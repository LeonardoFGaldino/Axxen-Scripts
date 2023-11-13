import fitz
import os
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog

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

def selecionar_pasta():
    global pasta_pdf
    pasta_pdf = filedialog.askdirectory()
    pasta_label.config(text=f"Pasta com PDFs: {pasta_pdf}")

def extrair_e_salvar():
    informacoes_pdf = []

    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith('.pdf'):
            pdf_path = os.path.join(pasta_pdf, arquivo)
            cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS, Valor_do_Pedido, CNPJ, Valor_Total_do_Documento = extrair_valores_cp(pdf_path)
            informacoes_pdf.append((arquivo, cp_terceiros, cp_segurados, cp_patronal, IRRF, IRPJ, CSLL, PIS, COFINS, Valor_do_Pedido, CNPJ, Valor_Total_do_Documento))


    df = pd.DataFrame(informacoes_pdf, columns=["Nome do Arquivo", "CP TERCEIROS", "CP SEGURADOS", "CP PATRONAL", "IRRF", "IRPJ", "CSLL", "PIS", "COFINS", "Valor_do_Pedido", "CNPJ", "Valor_Total_do_Documento"])


    excel_filename = "valores_cp.xlsx"
    df.to_excel(excel_filename, index=False)

    resultado_label.config(text=f'Valores extraídos e salvos em "{excel_filename}".')


root = tk.Tk()
root.title("Extração de Valores de PDF")


selecionar_button = tk.Button(root, text="Selecionar Pasta com PDFs", command=selecionar_pasta)
extrair_button = tk.Button(root, text="Extrair e Salvar", command=extrair_e_salvar, width=50)
pasta_label = tk.Label(root, text="Pasta com PDFs não selecionada.")
resultado_label = tk.Label(root, text="")



selecionar_button.pack()
pasta_label.pack()
extrair_button.pack()
resultado_label.pack()


root.mainloop()
