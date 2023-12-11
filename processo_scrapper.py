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

    AJAXREQUEST: _viewRoot
    fPP: numProcesso - inputNumeroProcessoDecoration:numProcesso - inputNumeroProcesso:
    mascaraProcessoReferenciaRadio: on
    fPP: j_id147:processoReferenciaInput:
    fPP: dnp:nomeParte:
    fPP: j_id165:nomeAdv:
    fPP: j_id174:classeProcessualProcessoHidden:
    tipoMascaraDocumento: on
    fPP: dpDec:documentoParte: 02.039
    .540 / 0001 - 04
    fPP: Decoration:numeroOAB:
    fPP: Decoration:j_id209:
    fPP: Decoration:estadoComboOAB: org.jboss.seam.ui.NoSelectionConverter.noSelectionValue
    fPP: fPP
    autoScroll:
    javax.faces.ViewState: j_id3
    fPP: j_id215: fPP: j_id215
    AJAX: EVENTS_COUNT: 1

    fetch("https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam", {
        "headers": {
            "accept": "*/*",
            "accept-language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        },
        "referrer": "https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": "AJAXREQUEST=_viewRoot&fPP%3AnumProcesso-inputNumeroProcessoDecoration%3AnumProcesso-inputNumeroProcesso=&mascaraProcessoReferenciaRadio=on&fPP%3Aj_id147%3AprocessoReferenciaInput=&fPP%3Adnp%3AnomeParte=&fPP%3Aj_id165%3AnomeAdv=&fPP%3Aj_id174%3AclasseProcessualProcessoHidden=&tipoMascaraDocumento=on&fPP%3AdpDec%3AdocumentoParte=06.160.091%2F0001-09&fPP%3ADecoration%3AnumeroOAB=&fPP%3ADecoration%3Aj_id209=&fPP%3ADecoration%3AestadoComboOAB=org.jboss.seam.ui.NoSelectionConverter.noSelectionValue&fPP=fPP&autoScroll=&javax.faces.ViewState=j_id8&fPP%3Aj_id215=fPP%3Aj_id215&AJAX%3AEVENTS_COUNT=1&",
        "method": "POST",
        "mode": "cors",
        "credentials": "include"
    });

headers = {
    'authority': 'pje1g.trf3.jus.br',
    'accept': '*/*',
    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'JSESSIONID2=w-jxUOONYLVx4Y_v3snfoIA4zZBzjabDJwEhaQ0X.svlpje21g15; PJECSID=6933531b90fdead9; ak_bmsc=73F20855BF5FD9522F62BC395CB03376~000000000000000000000000000000~YAAQFr7AFws9RbCLAQAARacURRbWtVvKXHoByyj3G6Trsr7p4T+7Epd1T8JqQQsDlOkFEJiQ1eccMHeIKA74+vVBro+I12DVIvkWRBLMT/12cOGVqA375SRlrZweMNhfzLZNyQa8M2LQoeD8+I8rRo1rd2qVWAsxRdK3iTMf5Y00x6FaZ2QdiGDT+/HZnFq1kJMc60QDeEKFUtwemlsWEQUiyAfQ94boNorDRjYOZTAWZKoQK9SZu39ljLctIMHwaKOFwbx8vFCZjaCnU8vcFi4BNrgCQoP5H320pvaw0UxffXAVxQHujK2N77b5pMODtxNDaJ0xd46sF3fNcG38jqf1FLKOoN4gCI0CZnoGdsXk41g2TWbc6P898jhKq6Q2RipbzaSnaUZzKsKmk6IgPhiKPir5Fn2Plp7UYlw/mds1ySwQoPhOWovGpZOLC7RyWx9gO9qsdKwtmft3OV01IZm+6PXF505qC5ISkZf/m0losr8hD9gGailIwAoGFbsliUkf; PJESID=65b7bd81909118f6; bm_sv=E1703A34B454BD60476393FA80620FEF~YAAQLr7AF2gjQbCLAQAADNcuRRb4gwjJBIGPEIItfRdksVcPVeNx6gVeAZkHf29KSpiUwqUHQXyGif5dPcx92IvIbV16edJwjwotDmMHcJlpQZh0V5XenvOXNUWloNmGS+a8F+XEjt/9riCLev9qUiVZeniaxZUyG3ItkwE/5FSM7z+drWlBj26vC+11LCBG4GPejK16fuUeucrlWkRKCavyuzI08XhTS4vtt5ZD2y6dLgSjpMbl/0F9PbexRR4FhY8=~1',
    'origin': 'https://pje1g.trf3.jus.br',
    'pragma': 'no-cache' ,
    'referer': 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

    curl 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam' -H 'authority: pje1g.trf3.jus.br' -H 'accept: */*' \
    -H 'accept-language: pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7' -H 'cache-control: no-cache' \
    -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'cookie: JSESSIONID2=w-jxUOONYLVx4Y_v3snfoIA4zZBzjabDJwEhaQ0X.svlpje21g15; PJECSID=6933531b90fdead9; ak_bmsc=73F20855BF5FD9522F62BC395CB03376~000000000000000000000000000000~YAAQFr7AFws9RbCLAQAARacURRbWtVvKXHoByyj3G6Trsr7p4T+7Epd1T8JqQQsDlOkFEJiQ1eccMHeIKA74+vVBro+I12DVIvkWRBLMT/12cOGVqA375SRlrZweMNhfzLZNyQa8M2LQoeD8+I8rRo1rd2qVWAsxRdK3iTMf5Y00x6FaZ2QdiGDT+/HZnFq1kJMc60QDeEKFUtwemlsWEQUiyAfQ94boNorDRjYOZTAWZKoQK9SZu39ljLctIMHwaKOFwbx8vFCZjaCnU8vcFi4BNrgCQoP5H320pvaw0UxffXAVxQHujK2N77b5pMODtxNDaJ0xd46sF3fNcG38jqf1FLKOoN4gCI0CZnoGdsXk41g2TWbc6P898jhKq6Q2RipbzaSnaUZzKsKmk6IgPhiKPir5Fn2Plp7UYlw/mds1ySwQoPhOWovGpZOLC7RyWx9gO9qsdKwtmft3OV01IZm+6PXF505qC5ISkZf/m0losr8hD9gGailIwAoGFbsliUkf; PJESID=65b7bd81909118f6; bm_sv=E1703A34B454BD60476393FA80620FEF~YAAQLr7AF2gjQbCLAQAADNcuRRb4gwjJBIGPEIItfRdksVcPVeNx6gVeAZkHf29KSpiUwqUHQXyGif5dPcx92IvIbV16edJwjwotDmMHcJlpQZh0V5XenvOXNUWloNmGS+a8F+XEjt/9riCLev9qUiVZeniaxZUyG3ItkwE/5FSM7z+drWlBj26vC+11LCBG4GPejK16fuUeucrlWkRKCavyuzI08XhTS4vtt5ZD2y6dLgSjpMbl/0F9PbexRR4FhY8=~1' \
    -H 'origin: https://pje1g.trf3.jus.br' -H 'pragma: no-cache' -H 'referer: https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam' \
    -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Windows"' -H 'sec-fetch-dest: empty' -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-site: same-origin' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
    --data-raw 'AJAXREQUEST=_viewRoot&fPP%3AnumProcesso-inputNumeroProcessoDecoration%3AnumProcesso-inputNumeroProcesso=&mascaraProcessoReferenciaRadio=on&fPP%3Aj_id147%3AprocessoReferenciaInput=&fPP%3Adnp%3AnomeParte=&fPP%3Aj_id165%3AnomeAdv=&fPP%3Aj_id174%3AclasseProcessualProcessoHidden=&tipoMascaraDocumento=on&fPP%3AdpDec%3AdocumentoParte=06.160.091%2F0001-09&fPP%3ADecoration%3AnumeroOAB=&fPP%3ADecoration%3Aj_id209=&fPP%3ADecoration%3AestadoComboOAB=org.jboss.seam.ui.NoSelectionConverter.noSelectionValue&fPP=fPP&autoScroll=&javax.faces.ViewState=j_id8&fPP%3Aj_id215=fPP%3Aj_id215&AJAX%3AEVENTS_COUNT=1&' \
    --compressed