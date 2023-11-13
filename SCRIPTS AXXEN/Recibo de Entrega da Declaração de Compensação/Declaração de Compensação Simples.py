import fitz  # PyMuPDF
import os
import re
import pandas as pd
import xml.etree.ElementTree as ET

pasta_pdf = 'C:\\Users\\Admin\\Desktop\\RECIBO'

def extrair_valores_cp(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()

        padrao = re.compile(r'CP TERCEIROS\s+([\d\.]+,\d+)|CP SEGURADOS\s+([\d\.]+,\d+)|CP PATRONAL\s+([\d\.]+,\d+)|IRRF\s+([\d\.]+,\d+)|IRPJ\s+([\d\.]+,\d+)|CSLL\s+([\d\.]+,\d+)|PIS\s+([\d\.]+,\d+)|COFINS\s+([\d\.]+,\d+)', re.IGNORECASE)
        valores_encontrados = padrao.findall(texto)

        cp_terceiros = ""
        cp_segurados = ""
        cp_patronal = ""
        IRRF = ""
        IRPJ = ""
        CSLL = ""
        PIS = ""
        COFINS = ""


        for match in valores_encontrados:
            if match[0]:
                cp_terceiros = match[0]
            elif match[1]:
                cp_segurados = match[1]
            elif match[2]:
                cp_patronal = match[2]
            elif match[3]:
                IRRF = match[3]
            elif match[4]:
                IRPJ = match[4]
            elif match[5]:
                CSLL = match[5]
            elif match[6]:
                PIS = match[6]
            elif match[7]:
                COFINS = match[7]


        return cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS
    except Exception as e:
        print(f"Erro ao extrair informações do PDF: {str(e)}")
        return "", "", ""

informacoes_pdf = []

for arquivo in os.listdir(pasta_pdf):
    if arquivo.endswith('.pdf'):
        pdf_path = os.path.join(pasta_pdf, arquivo)
        cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS = extrair_valores_cp(pdf_path)
        informacoes_pdf.append((arquivo, cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS))

# Criar um DataFrame
df = pd.DataFrame(informacoes_pdf, columns=["Nome do Arquivo", "CP TERCEIROS", "CP SEGURADOS", "CP PATRONAL", "IRRF", "IRPJ", "CSLL", "PIS", "COFINS"])

# Salvar DataFrame em um arquivo Excel
df.to_excel("valores_cp.xlsx", index=False)

print('Valores extraídos e salvos em "valores_cp.xlsx".')
