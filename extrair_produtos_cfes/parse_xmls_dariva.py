import os
import logging
import multiprocessing as mp
from dataclasses import dataclass
import xml.etree.ElementTree as ET
from glob import glob
from tqdm.contrib.concurrent import process_map
from typing import List, Iterable
import re
import sqlite3
from abc import ABC
from contextlib import contextmanager
import argparse

# regex para identificação de data
DATE_REGEX = r'20\d\d[01]\d[0123]\d'
# base com classificação de ncms (monofasico, tributado ou analisar)
MONOFASIA_DB = './monofasia.db'
# nome da tabela de classificacao de ncms
MONOFASIA_TB = 'ncms'
# formato do log
LOG_FMT='%(asctime)s |%(levelname)s|-> %(message)s'

# nome da tabela dos ncms
TABLENAME='cfes'

class TagI(ABC):
    """ Interface de classe de tags de xml de documentos fiscais """
    base_info:dict
    product_root:str
    product_info:dict

    @classmethod
    def headers(self):
        pass

    @classmethod
    def column_count(self):
        pass

@dataclass
class TagsCfe(TagI):
    base_info = {
        'modelo': './/{*}ide/mod',
        'cnpj_emitente': './/{*}emit/CNPJ',
        'nome_emitente': './/{*}emit/xNome',
        'data_emissao': './/{*}ide/dEmi',
        'destinatario': './/{*}dest/xNome',
        'vl_total_produtos': './/{*}total/vCFe',
        'vl_total_lei_12741': './/{*}total/vCFeLei12741'
    }
    product_root = './/{*}det'
    product_info = {
        'nome_prod': './/{*}prod/xProd',
        'ncm': './/{*}prod/NCM',
        'cfop': './/{*}prod/CFOP',
        'vl_unitario': './/{*}prod/vUnCom',
        'vl_prod': './/{*}prod/vProd',
        'vl_desconto': './/{*}prod/vDesc',
        'vl_item': './/{*}prod/vItem',
        'qnt_item': './/{*}prod/qCom',
        'cest': './/{*}prod/obsFiscoDet/xTextoDet'
    }

    @classmethod
    def headers(cls):
        base = list(cls.base_info.keys())
        products = list(cls.product_info.keys())
        headers = base + products
        headers.append('hiperlink')
        return headers
    
    @classmethod
    def column_count(cls):
        base = len(cls.base_info)
        products = len(cls.product_info)
        return base + products + 1

def search_tag(root_node: ET.Element, tag: str, ns:dict={'': '*'}) -> str:
    """ Busca tag em node raiz """
    text = root_node.findtext(tag, default='', namespaces=ns)

    is_date = re.fullmatch(DATE_REGEX, text) is not None
    is_number = all(c.isdigit() for c in text.replace('.', '', 1)) and not is_date

    if is_number:
        text = text.replace('.', ',')
    elif is_date:
        y = text[:4]
        m = text[4:6]
        d = text[6:]

        text = f'{d}/{m}/{y}'

    text = text.encode('latin-1', errors='xmlcharrefreplace').decode('latin-1')
    text = text.replace(';', ' ')    
    return text


@contextmanager
def get_db_conn(columns:List[str], filepath=None) -> sqlite3.Connection:
    """Cria uma base sqlite3 (no disco caso filepath seja passado, e na memoria caso contrario)"""

    # xml table columns
    columns = TagsCfe.headers()
    column_names = f"', '".join(columns)
    column_names = f"'{column_names}'"

    conn = None

    # db file
    db_file = filepath or ':memory:'

    try:
        conn = sqlite3.connect(db_file)
        # disabling synchronous operations
        conn.execute('PRAGMA synchronous = OFF')
        # connecting to monofasia database
        monofasia_conn = sqlite3.connect(MONOFASIA_DB)
        # backing up monofasia to in memory db
        monofasia_conn.backup(conn)
        # close monofasia conection
        monofasia_conn.close()
        # create query
        query = f'CREATE TABLE {TABLENAME} ({column_names});'
        # create xml table
        conn.execute(query)
        yield conn
    finally:
        if conn:
            conn.close()
    
def parse_xml(filepath:str, tags:TagI=TagsCfe) -> List[tuple]:
    """ Faz parse de arquivo xml """
    # definindo hiperlink
    hiperlink = f'=HIPERLINK("{filepath}")'

    # abrindo xml
    tree = ET.parse(filepath)
    root = tree.getroot()

    # criando listas
    ctf_rows = []
    ctf_data = []
    
    # iterando tags exclusivas por nota
    for value in tags.base_info.values():
        tag_value = search_tag(root, value)
        ctf_data.append(tag_value)

    product_root_tag = tags.product_root
    # iterando todos produtos da nota
    for product_root_node in root.iterfind(product_root_tag, namespaces={'': '*'}):
        product_data = []
        # iterando tags de produto
        for product_tag in tags.product_info.values():
            value = search_tag(product_root_node, product_tag)
            product_data.append(value)
        product_data = ctf_data + product_data
        # add caminho para arquivo a linha do produto
        product_data.append(hiperlink)    
        row = tuple(product_data)
        ctf_rows.append(row)
    return ctf_rows

def get_files(root_path):
    """ Busca arquivos em pasta """
    logger = logging.getLogger()
    logger.info(f'Buscando xmls em {root_path}...')
    
    # busca arquivos na pasta
    regex = os.path.join(root_path, '**', '*.xml')
    file_list = glob(regex, recursive=True)
    logger.info(f'Total de {len(file_list)} xmls encontrados.')
    return file_list

def extract_xml_data(xmls:List[str], tags:TagI=TagsCfe) -> list:
    """ Busca todos os arquivos de xml da pasta e extrai informações """
    # get cpu count for mp
    cpus = os.cpu_count()*2
    
    # definindo chunksize
    cs = len(xmls)//(cpus*5)
    cs = max(1, cs)

    # processing files
    nfs = process_map(parse_xml, xmls, max_workers=cpus, chunksize=cs)

    # extraindo tuplas das nfs
    products = [product_tuple for nf in nfs for product_tuple in nf]
    return products

def save_csv(data:List[Iterable[str]], header_row:List[str], target_file:str='output.csv'):
    """ Funcao para salvar tabela de ncms """
    logger = logging.getLogger()
    # inserindo headers na lista de linhas do arquivo e preparando string para csv
    csv_rows = [';'.join([str(col) if col else '' for col in row]) for row in data]
    # insert header row into csv row list
    csv_rows.insert(0, header_row)
    # generate csv file content
    csv_content = '\n'.join(csv_rows)
    # write output to file
    open(target_file, 'w', encoding='latin-1').write(csv_content)
    logger.info(f'O csv foi salvo em "{target_file}"...')

def insere_xml_sqlite(conn:sqlite3.Connection, xml_data:List[tuple]):
    """ Funcao para salvar informacoes extraidas do xml na base sqlite para classificacao por ncms"""   
    # montando query
    values = ','.join(['?' for _ in range(TagsCfe.column_count())])
    column_names = ", ".join(TagsCfe.headers())
    query = f'INSERT INTO {TABLENAME} ({column_names}) VALUES ({values});'
    
    # criando iterador
    iterator = iter(xml_data)
    # inserindo na base
    conn.executemany(
        query,
        iterator
    )
    conn.commit()

def classifica_ncm_sqlite(
        conn:sqlite3
    ):
    """ funcao para classificar ncms entre MONOFASICO, ANALISE e TRIBUTADO"""
    #montando query
    selection = [f'{TABLENAME}.{col}' for col in TagsCfe.headers()]
    selection.append(f'{MONOFASIA_TB}.classificacao')
    selection = ', '.join(selection)

    query = f'SELECT {selection} FROM {TABLENAME} LEFT JOIN {MONOFASIA_TB} ON {MONOFASIA_TB}.ncm = {TABLENAME}.ncm WHERE {MONOFASIA_TB}.classificacao IS NOT NULL;'
    cur = conn.execute(query)
    # buscando resultados
    data = cur.fetchall()
    return data

def main(xmls_dir:str, output_file:str):
    """ Funcao main """
    logger = logging.getLogger()
    # busca arquivos na pasta xmls_dir    
    xml_filelist = get_files(root_path=xmls_dir)

    # extrai dados xml
    logger.info('Iniciando processamento de arquivos...')
    xml_data = extract_xml_data(xml_filelist)
    # get headers
    headers=TagsCfe.headers()
    headers.append('arquivo')

    # cria base na memória com ncms classificados e tabela de xmls vazia
    with get_db_conn(headers) as conn:
        logger.info('Preparando dados...')
        # popula tabela de dados de xmls
        insere_xml_sqlite(conn, xml_data)
        # classifica ncms
        logger.info('Classificando NCMs...')
        data_with_class = classifica_ncm_sqlite(conn)
        
    # gera headers para csv
    tag_keys = TagsCfe.headers()
    tag_keys.append('classificacao')
    csv_header_row = ';'.join(tag_keys)
    # salva csv
    save_csv(
        data=data_with_class, 
        target_file=output_file, 
        header_row=csv_header_row
    )
    logging.info('Encerrando...')

def parser_setup():
    """ Configura argparser """
    arg_parser = argparse.ArgumentParser(
        prog='Parser de XMLs',
        description='Script para extrair informações referentes a produtos das notas e classificar respectivos ncms entre MONOFASICOS, TRIBUTADOS E ANALISE.'
    )
    
    arg_parser.add_argument('-d', '--directory', required=True)
    arg_parser.add_argument('-v', '--verbose', action='store_true')
    arg_parser.add_argument('-o', '--output', default='output.csv')
    return arg_parser

if __name__ == '__main__':
    arg_parser = parser_setup()
    args = vars(arg_parser.parse_args())
    current_dir = os.getcwd()
    # get root_dir
    root_dir = os.path.join(current_dir, args['directory'])
    # get output_file
    output_file = os.path.join(current_dir, args['output'])
    # get log level
    LOG_LVL = logging.INFO if args['verbose'] else logging.ERROR


    logging.basicConfig(
        level=LOG_LVL, 
        format=LOG_FMT
    )
    if root_dir and output_file:
        main(xmls_dir=root_dir, output_file=output_file)
