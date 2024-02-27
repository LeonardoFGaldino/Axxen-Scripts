from glob import glob
import fitz
import re


pasta = r'P:\13 - PROJETOS\006.011\DOCUMENTOS FISCAIS\DOC. FISCAL COMPLEMENTAR\ENERGIA ELÉTRICA'
arquivos = glob('**/*.pdf', recursive=True)
texto = '\n'.join(p.get_text() for p in fitz.open(arquivos[0]))
campos = {}

# teste dos regexs:

# re.search(r'CNPJ:\s*(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})', texto)
# m = re.search(r'CNPJ:\s*(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})', texto)
# m.groups()[0]


# grupo dos regexs:

regexes = {
'Data de Emissão': r'\s*(\d{2}/\d{2}/\d{4})',
'Total Consolidado': r'Total Consolidado\s*([\d.]+\,\d{2})',
'CNPJ': r'CNPJ:\s*(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})',
'Série': r'Série ([^\s]*)',
'Número do Documento': r'N\º (\d{9})'}



def extrai_campos(doc, regexes):
    text = '\n'.join(p.get_text() for p in fitz.open(doc))
    campos = {}
    for k, v in regexes.items():
        m = re.search(v, text)
        valor = m.groups()[0] if m else ''
        campos[k] = valor
    return campos


valores = [extrai_campos(d, regexes) for d in arquivos]


resultado = {}
for d in valores:
    for k, v in d.items():
        if k not in resultado.keys():
            resultado[k] = []
        resultado[k].append(v)


rows = list(zip(*resultado.values()))

rows.insert(0, list(resultado.keys()))

csv_content = '\n'.join([';'.join(r) for r in rows])

open('resultado.csv', 'w').write(csv_content)



# o arquivo vai ser salvo na pasta .py


















