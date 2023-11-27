import re
import fitz
import pandas as pd
from glob import glob


def extrai(documentos, lista_regexes, filename):
    valores = {}
    for documento in documentos:
        for header, regex in lista_regexes.items():
            value = search_regex(regex, documento)
            if header not in valores:
                valores[header] = []
            valores[header].append(value)

    valores['Arquivo'] = [f'=hiperlink("{filename}")'] * len(documentos)

    return valores


def le_arquivo(filename: str):
    texto = '\n'.join(p.get_text() for p in fitz.open(filename))
    return texto


def search_regex(regex, content):
    m = re.search(regex, content)
    if not m:
        return ''
    return m.groups()[0]


def salva_arquivo(resultado: dict, filename: str):
    df = pd.DataFrame(resultado)
    df.to_excel(filename, index=False)


def parse_arquivo(filename: str, regexes: dict, target_file: str, regexes_gerais: dict):
    content = le_arquivo(filename)
    content = content.split('Página 8')[-1]

    documentos = re.split(r'\d{4}\.', content)[1:]

    dicionario = extrai(documentos, regexes, filename)
    return dicionario


def concatena_dicts(dict1, dict2):
    if len(dict1) == 0:
        return dict2
    for chave, coluna in dict2.items():
        if chave not in dict1:
            raise ValueError
        dict1[chave].extend(coluna)
    return dict1


def main(lista_arquivos):
    regexes_gerais = {
        'Período de Apuração do Arquivo': r'(?<=Período apuração )(\d{2}\/\d{4})',
        'Número do Recibo': r'(?<=Número do Recibo )([\d]*)',
        'Data/Hora da Transmissão ': r'(?<=Data/Hora da Transmissão )(\d{2}\/\d{2}\/\d{4} \d{2}\:\d{2}\:\d{2})'
    }
    regexes = {
        'CNPJ Emitente': r'(?<=CNPJ do Emitente: )(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})',
        'N° da Nota Fiscal': r'(?<=N° da Nota Fiscal: )([\d]*)',
        'Data de Emissão': r'(?<=Data de Emissão : )(\d{2}/\d{2}/\d{4})',
        'CFOP': r'(?<=CFOP: )(\d+\.\d+ - .*)[\n\r]*',
        'Espécie do crédito': r'(?<=Espécie do crédito : )([^\n]*)',
        'Período de Escrituração do Crédito': r'(?<=Período de Escrituração do Crédito : )([^\n]*)',
        'Valor Total': r'(?<=Valor Total)[\s\t]*([\d\.]*\,\d{2})',
        'Valor do IPI Destacado': r'(?<=Valor do IPI Destacado)([\s\t]*[\d\.]*\,\d{2})',
        'Valor do IPI Creditado no Livro RAIPI': r'(?<=Valor do IPI Creditado no Livro RAIPI)([\s\t]*[\d\.]*\,\d{2})'
    }
    valores = {}
    for filepath in lista_arquivos:
        resultado = parse_arquivo(filepath, regexes, '../resultado2.csv', regexes_gerais)
        valores = concatena_dicts(valores, resultado)
    salva_arquivo(valores, 'ISAIASREGEX.xlsx')


if __name__ == '__main__':
    main(['./IPI SANDEPAR.pdf'])
