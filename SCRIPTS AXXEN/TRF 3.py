import requests as req
from bs4 import BeautifulSoup as bs
from time import sleep
from tqdm import tqdm
import re

URI = 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam'


def limpa_url(url):
    url = url.strip('openPopUp(\'Consulta pública\',\'').strip('\')')
    url = 'https://pje1g.trf3.jus.br' + url
    return url

def get_urls(response):
    soup = bs(response.text)
    if soup.find(string='Sua pesquisa não encontrou nenhum processo disponível.'):
        return []
    links = soup.find_all('a', attrs={'title': 'Ver Detalhes'})
    urls = [link.attrs['onclick'] for link in links]
    urls = [limpa_url(url) for url in urls]
    return urls

def extrai_num_processo(soup):
    parent_div = soup.find(id='j_id131:processoTrfViewView:j_id137')
    target = parent_div.find('div', attrs={'class': 'col-sm-12'})
    text = target.get_text().strip()
    return text

def extrai_classe(soup):
    parent_div = soup.find(id='j_id131:processoTrfViewView:j_id160')
    target = parent_div.find('div', attrs={'class': 'col-sm-12'})
    text = target.get_text().strip()
    text = re.sub(r'[\n]+', ' | ', text)
    return text

def extrai_assunto(soup):
    parent_div = soup.find(id='j_id131:processoTrfViewView:j_id171')
    target = parent_div.find('div', attrs={'class': 'col-sm-12'})
    text = target.get_text().strip()
    text = re.sub(r'[\n]+', ' | ', text)
    return text

def extrai_exequente(soup):
    exequente = soup.find('span', attrs={'id': 'j_id131:processoPartesPoloAtivoResumidoList:0:j_id278'})
    exequente = exequente.get_text().strip()
    exequente = re.sub(r'[\n]+', ' | ', exequente)
    return exequente

def extrai_executado(soup):
    executado = soup.find('span', attrs={'id': 'j_id131:processoPartesPoloPassivoResumidoList:0:j_id342'})
    executado = executado.get_text().strip()
    executado = re.sub(r'[\n]+', ' | ', executado)
    return executado

def extrai_atualizacao(soup):
    atualizacao = soup.find(id='j_id131:processoEvento:0:j_id492').get_text().strip()
    return atualizacao

def extrai_processos_info(res):
    soup = bs(res.text)
    valores = {
        'Número Processo': extrai_num_processo(soup),
        'Classe': extrai_classe(soup),
        'Assuntos': extrai_assunto(soup),
        'Exequente': extrai_exequente(soup),
        'Executado': extrai_executado(soup),
        'Ultima Atualização': extrai_atualizacao(soup),
        'Link para o processo': res.url
    }
    return valores

def extrai_processos(processos, headers):
    dados = {}
    for processo in tqdm(processos):
        res = req.get(processo, headers=headers, timeout=5)
        valores = extrai_processos_info(res)
        for key, value in valores.items():
            if key not in dados:
                dados[key] = []
            dados[key].append(value)
        sleep(0.6)
    return dados

def dict_to_csv(dados:dict):
    headers = dados.keys()
    body = list(zip(*dados.values()))
    body.insert(0, headers)
    csv = '\n'.join(';'.join(row) for row in body)
    return csv
def formata_cnpj(cnpj):
    cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[-2:]
    return cnpj

def main(cnpj):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    cnpj_fmt = formata_cnpj(cnpj)
    data = {
        'AJAXREQUEST': '_viewRoot',
        'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso': '',
        'mascaraProcessoReferenciaRadio': 'on',
        'fPP:j_id147:processoReferenciaInput': '',
        'fPP:dnp:nomeParte': '',
        'fPP:j_id165:nomeAdv': '',
        'fPP:j_id174:classeProcessualProcessoHidden': '',
        'tipoMascaraDocumento': 'on',
        'fPP:dpDec:documentoParte': cnpj_fmt,
        'fPP:Decoration:numeroOAB': '',
        'fPP:Decoration:j_id209': '',
        'fPP:Decoration:estadoComboOAB': 'org.jboss.seam.ui.NoSelectionConverter.noSelectionValue',
        'fPP': 'fPP',
        'autoScroll': '',
        'javax.faces.ViewState': 'j_id1',
        'fPP:j_id215': 'fPP:j_id215 ',
        'AJAX:EVENTS_COUNT': '1',
    }
    session = req.Session()
    res = session.get(URI, headers=headers, timeout=5)
    headers = {
        'authority': 'pje1g.trf3.jus.br',
        'accept': '*/*',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pje1g.trf3.jus.br',
        'pragma': 'no-cache',
        'referer': 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    cookies = dict(session.cookies)
    res = req.post(URI, data=data, cookies=cookies, headers=headers, timeout=5)
    urls = get_urls(res)
    dados = extrai_processos(urls, headers)
    csv = dict_to_csv(dados)
    open(f'relatorio_processos_{cnpj}.csv', 'w').write(csv)

if __name__ == '__main__':
    main('06160091000109')









