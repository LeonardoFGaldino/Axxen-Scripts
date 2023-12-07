import requests as req
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
from time import sleep
import requests

URI = 'https://eproc.jfrj.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica&acao_origem=processo_seleciona_publica&acao_retorno=processo_consulta_publica&hash=a72c988fb3b414b5e622827d64a238e3'

def get_post_data(res, cnpj):
    soup = bs(res.text, features='lxml')
    
    data = {}
    cnpj_name = soup.find('input', attrs={'onkeypress': 'mascaraCpfCnpj(this,event);'}).attrs['name']
    checkbox_name = soup.find('input', attrs={'checked': 'checked'}).attrs['name']
    radio_name = soup.find('input', attrs={'onclick': 'trocarCpfCnpj();'}).attrs['name']
    
    inputs = soup.find(id='divInfraAreaDados').find_all('input')
    input_names = [i.attrs['name'] for i in inputs]
    values = ['']*len(input_names)
    
    input_values = dict(zip(input_names, values))
    
    input_values[radio_name] = 'CNPJ'
    input_values[cnpj_name] = cnpj
    input_values[checkbox_name]= 'S'
    
    input_values['hdnInfraTipoPagina'] = '1'
    input_values['hdnInfraSelecoes'] = 'Infra'
    input_values['sbmNovo'] = 'Consultar'

    return input_values


def get_urls(data, cookies, headers):
    res = requests.post(URI, data=data, cookies=cookies, headers=headers)
    soup = bs(res.text, features='lxml')
    table = soup.find(id='divInfraAreaTabela').find('table')
    links = table.find_all('a')
    
    raiz_uri = '/'.join(URI.split('/')[:-1])
    uris = [f'{raiz_uri}/{link.attrs["href"]}' for link in links]
    return uris

def limpa_cnpj(cnpj):
    cnpj = (
        cnpj
            .replace('.', '')
            .replace('/', '')
            .replace('-', '')
        )
    return cnpj

def extrai_processo_info(uri:str):
    res = requests.get(uri)
    soup = bs(res.text, features='lxml')
    classe = soup.find('span', attrs={'id': 'txtClasse'})
    
    num_processo = soup.find(id='txtNumProcesso').get_text()
    situacao = soup.find(id='txtSituacao').get_text()
    
    classe = soup.find(id='txtClasse').get_text()
    
    assuntos_soup = soup.find_all(id='fldAssuntos')[1].find('table')
    assuntos_linhas = assuntos_soup.find_all('tr')
    assuntos_cells = [tr.find_all('td') for tr in assuntos_linhas]
    assuntos = [' - '.join(td.get_text() for td in tr[:-1]) for tr in assuntos_cells][1:] # [1:] para remover th's
    assuntos = ' | '.join(assuntos)
    
    partes = soup.find(id='fldPartes')
    partes_tb = partes.find('table')
    partes = partes_tb.find_all('tr')[1]
    
    exequente, executado = [td.get_text().strip('    - ') for td in partes.find_all('td')]
    
    atualizacoes_table = soup.find_all('table', attrs={'width': '95%', 'class': 'infraTable', 'summary': 'Assuntos'})[-1]
    ultima_atualizacao = atualizacoes_table.find_all('tr')[1].find_all('td')[1]
    atualizacao = ultima_atualizacao.get_text()
    
    return  {
        'Número do Processo': num_processo,
        'classe': classe,
        'Situação': situacao,
        'Assuntos': assuntos,
        'Exequente': exequente,
        'Executado': executado,
        'Ultima Atualização': atualizacao,
        'Link para o processo': uri
    }

def extrai_processos(lista_processos):
    dados = {}
    for uri in tqdm(lista_processos):
        processo_dados = extrai_processo_info(uri)
        sleep(.6)
        for k, v in processo_dados.items():
            if k not in dados.keys():
                dados[k] = []
            dados[k].append(v)
    return dados

def dict_to_csv(dados:dict):
    headers = dados.keys()
    body = list(zip(*dados.values()))    
    body.insert(0, headers)
    csv = '\n'.join(';'.join(row) for row in body)
    return csv
    
def main(cnpj):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    session = requests.Session()
    response = session.get(URI)
    data = get_post_data(response, cnpj)
    cookies = dict(session.cookies)
    processos_uris = get_urls(data=data, headers=headers, cookies=cookies)
    dados = extrai_processos(processos_uris)
    csv = dict_to_csv(dados)
    open(f'relatorio_processos_{cnpj}.csv', 'w').write(csv)

if __name__ == '__main__':
    main('02039540000104')