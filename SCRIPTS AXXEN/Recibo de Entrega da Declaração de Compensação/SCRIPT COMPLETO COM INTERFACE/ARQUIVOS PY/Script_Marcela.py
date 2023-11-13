import os
import fitz
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Entry
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

colunas = ['Período', 'Código', 'Descrição', 'Principal', 'Nome do Arquivo']
df = pd.DataFrame(columns=colunas)

def le_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    rows = []
    for pagina in doc:
        pagina = pagina.get_text()
        match = re.search(r'([0123]\d\/[01]\d\/\d{4})\n(?=[0123]\d\/[01]\d\/\d{4}\n\d{17}\nCNPJ)', pagina)
        if match:
            periodo = match.group(1)
            valores = re.findall(r'\n(1170|1176|1181|1184|1200|1213|1218|1191|1196|)\n([^\d^\n]*)\n([\d.]*,\d{2})', pagina)
            valores = [list(linha) for linha in valores if all(linha)]
            [linha.insert(0, periodo) for linha in valores]
            rows.extend(valores)
    df = pd.DataFrame(rows, columns=['Período', 'Código', 'Descrição', 'Principal'])
    df['Principal'] = df['Principal'].apply(lambda valor: float(valor.replace('.', '').replace(',', '.')))
    return df

def selecionar_pasta():
    global pasta_pdf
    pasta_pdf = filedialog.askdirectory()
    pasta_label.config(text=f"Pasta com PDFs: {pasta_pdf}")

def selecionar_pasta_destino():
    global pasta_destino
    pasta_destino = filedialog.askdirectory()
    pasta_destino_label.config(text=f"Pasta de Destino: {pasta_destino}")

def extrair_e_salvar():
    global df
    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith('.pdf'):
            pdf_path = os.path.join(pasta_pdf, arquivo)
            valores_encontrados = le_pdf(pdf_path)
            if not valores_encontrados.empty:
                valores_encontrados['Nome do Arquivo'] = arquivo
                df = pd.concat([df, valores_encontrados], ignore_index=True)

    resultado_label.config(text="")
    if df.empty:
        resultado_label.config(text="Nenhum dado encontrado nos PDFs.")
        return


    total_geral_por_arquivo = df.groupby('Nome do Arquivo')['Principal'].sum().reset_index()
    total_geral_por_arquivo['Período'] = 'Total Geral'
    total_geral_por_arquivo['Código'] = ''
    total_geral_por_arquivo['Descrição'] = ''


    df = pd.concat([df, total_geral_por_arquivo], ignore_index=True)

    if not pasta_destino:
        resultado_label.config(text="Por favor, selecione uma pasta de destino.")
        return

    nome_arquivo = nome_arquivo_entry.get().strip()

    if not nome_arquivo:
        resultado_label.config(text="Por favor, insira um nome de arquivo.")
        return

    if not nome_arquivo.endswith(".xlsx"):
        nome_arquivo += ".xlsx"

    excel_filename = os.path.join(pasta_destino, nome_arquivo)
    df.to_excel(excel_filename, index=False)
    resultado_label.config(text=f'Valores extraídos e salvos em "{excel_filename}"')

root = tk.Tk()
root.title("Extração de Valores de PDF")

selecionar_button = tk.Button(root, text="Selecionar Pasta com PDFs", command=selecionar_pasta)
selecionar_destino_button = tk.Button(root, text="Selecionar Pasta de Destino", command=selecionar_pasta_destino)
extrair_button = tk.Button(root, text="Extrair e Salvar", command=extrair_e_salvar, width=50)
pasta_label = tk.Label(root, text="Pasta com PDFs não selecionada.")
pasta_destino_label = tk.Label(root, text="Pasta de Destino não selecionada.")
resultado_label = tk.Label(root, text="")

nome_arquivo_label = tk.Label(root, text="Nome do arquivo de saída:")
nome_arquivo_entry = Entry(root)

selecionar_button.pack()
selecionar_destino_button.pack()
pasta_label.pack()
pasta_destino_label.pack()
nome_arquivo_label.pack()
nome_arquivo_entry.pack()
extrair_button.pack()
resultado_label.pack()

root.mainloop()
