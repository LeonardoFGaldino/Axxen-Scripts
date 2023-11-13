import fitz
import os
import re
import pandas as pd
import xml.etree.ElementTree as ET

pasta_pdf = 'C:\\Users\\Admin\\Desktop\\TESTE'

def extrair_valores_cp(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()


        padrao = re.compile(

            r'CP TERCEIROS\s+([\d\.]+,\d+)'
            r'|CP SEGURADOS\s+([\d\.]+,\d+)'
            r'|CP PATRONAL\s+([\d\.]+,\d+)'
            r'|IRRF\s+([\d\.]+,\d+)'
            r'|IRPJ\s+([\d\.]+,\d+)'
            r'|CSLL\s+([\d\.]+,\d+)'
            r'|PIS\s+([\d\.]+,\d+)'
            r'|COFINS\s+([\d\.]+,\d+)'
            r'|Valor do Pedido:\s+([\d\.]+,\d+)'
            r'|CNPJ:\s*(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})'
            r'|Valor Total do Documento\s+([\d\.]+,\d+)'

            , re.IGNORECASE

        )

        valores_encontrados = padrao.findall(texto)

        cp_terceiros = ""
        cp_segurados = ""
        cp_patronal = ""
        IRRF = ""
        IRPJ = ""
        CSLL = ""
        PIS = ""
        COFINS = ""
        Valor_do_Pedido = ""
        CNPJ = ""
        Valor_Total_do_Documento = ""


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
            elif match[8]:
                Valor_do_Pedido = match[8]
            elif match[9]:
                CNPJ = match[9]
            elif match[10]:
                Valor_Total_do_Documento = match[10]



        return cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS, Valor_do_Pedido, CNPJ, Valor_Total_do_Documento
    except Exception as e:
        print(f"Erro ao extrair informações do PDF: {str(e)}")
        return "", "", ""

informacoes_pdf = []

for arquivo in os.listdir(pasta_pdf):
    if arquivo.endswith('.pdf'):
        pdf_path = os.path.join(pasta_pdf, arquivo)
        cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS, Valor_do_Pedido, CNPJ, Valor_Total_do_Documento = extrair_valores_cp(pdf_path)
        informacoes_pdf.append((arquivo, cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS, Valor_do_Pedido, CNPJ, Valor_Total_do_Documento))

# Criar um DataFrame
df = pd.DataFrame(informacoes_pdf, columns=["Nome do Arquivo", "CP TERCEIROS", "CP SEGURADOS", "CP PATRONAL", "IRRF", "IRPJ", "CSLL", "PIS", "COFINS", "Valor_do_Pedido", "CNPJ", "Valor_Total_do_Documento"])

# Salvar DataFrame em um arquivo Excel
df.to_excel("valores_cp.xlsx", index=False)

print('Valores extraídosss e salvos em "valores_cp.xlsx".')