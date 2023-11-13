import re
import fitz
from glob import glob


def extrai(documentos, valores_gerais, lista_regexes, filename):
    valores = {}
    for documento in documentos:
        for header, regex in lista_regexes.items():
            value = search_regex(regex, documento)
            if header not in valores:
                valores[header] = []
            valores[header].append(value)
    
    for header, valor in valores_gerais.items():
        valores[header] = [f'="{valor}"'] * len(documentos)
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
    headers = resultado.keys()
    values = list(zip(*resultado.values()))
    values.insert(0, headers)
    values = [';'.join(row) for row in values]
    csv_string = '\n'.join(values)
    open(filename, 'w').write(csv_string)


def parse_arquivo(filename: str, regexes: dict, target_file: str, regexes_gerais:dict):
    content = le_arquivo(filename)
    content_geral, *documentos = content.split('Débito Apurado e Crédito Vinculado')

    valores_gerais = {}
    for key, regex in regexes_gerais.items():
        valores_gerais[key] = search_regex(regex, content_geral)

    dicionario = extrai(documentos, valores_gerais, regexes, filename)
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
      'Código da Receita': r'(?<=Código da Receita )(\d{4}-\d{2})',
      'Débito Apurado':  r'(?<=Débito Apurado )([\d.]+\,\d{2})',
      'Descrição': r'(?<=Descrição )([^\n]+)',
      'Período Apuração Débito': r'(?<=Período Apuração Débito)([^\n]+)',
      'Salário Familia': r'(?<=Salário Família: )([\d.]+\,\d{2})',
      'Retenção Lei 9711/98': r'(?<=Retenção Lei 9711/98: )([\d.]+\,\d{2})',
      'Saldo a Pagar': r'(?<=Saldo a Pagar )([\d.,]+\d{2})'
    }
    valores = {}
    for filepath in lista_arquivos:
        resultado = parse_arquivo(filepath, regexes, '../resultado2.csv', regexes_gerais)
        valores = concatena_dicts(valores, resultado)
    salva_arquivo(valores, '..resultado.csv')


if __name__ == '__main__':
    main(['../f.pdf', '../f2.pdf'])