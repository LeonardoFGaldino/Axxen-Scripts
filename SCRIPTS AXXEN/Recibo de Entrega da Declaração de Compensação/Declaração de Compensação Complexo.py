import fitz
import os
import re
import pandas as pd
from enum import Enum

pasta_pdf = 'C:\\Users\\Admin\\Desktop\\RECIBO'

class Campos(Enum):
    CP_TERCEIROS = ("CP TERCEIROS", re.compile(r'CP TERCEIROS\s+([\d\.]+,\d+)', re.IGNORECASE))
    CP_SEGURADOS = ("CP SEGURADOS", re.compile(r'CP SEGURADOS\s+([\d\.]+,\d+)', re.IGNORECASE))
    CP_PATRONAL = ("CP PATRONAL", re.compile(r'CP PATRONAL\s+([\d\.]+,\d+)', re.IGNORECASE))
    IRRF = ("IRRF", re.compile(r'IRRF\s+([\d\.]+,\d+)', re.IGNORECASE))
    IRPJ = ("IRPJ", re.compile(r'IRPJ\s+([\d\.]+,\d+)', re.IGNORECASE))
    CSLL = ("CSLL", re.compile(r'CSLL\s+([\d\.]+,\d+)', re.IGNORECASE))
    PIS = ("PIS", re.compile(r'PIS\s+([\d\.]+,\d+)', re.IGNORECASE))
    COFINS = ("COFINS", re.compile(r'COFINS\s+([\d\.]+,\d+)', re.IGNORECASE))

def extrair_valores_cp(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()

        valores = {}

        for campo in Campos:
            regex = campo.value[1]
            campo = campo.value[0]
            match = regex.search(texto) or ''
            if match:
                match = match.group(1)
            valores[campo] = match
        lista_valores = list(valores.values())
        return lista_valores
    except Exception as e:
        print(f"Erro ao extrair informações do PDF: {str(e)}")
        #raise e
        return [""] * len(Campos)

informacoes_pdf = []

for arquivo in os.listdir(pasta_pdf):
    if arquivo.endswith('.pdf'):
        pdf_path = os.path.join(pasta_pdf, arquivo)
        valores = extrair_valores_cp(pdf_path)
        informacoes_pdf.append([arquivo] + valores)

# Criar um DataFrame
colunas = ["Nome do Arquivo"] + [campo.name for campo in Campos]
df = pd.DataFrame(informacoes_pdf, columns=colunas)

# Salvar DataFrame em um arquivo Excel
df.to_excel("valores_cp.xlsx", index=False)

print('Valores extraídos e salvos em "valores_cp.xlsx".')
