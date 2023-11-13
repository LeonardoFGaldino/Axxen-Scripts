import os
import xml.etree.ElementTree as ET
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from glob import glob
import multiprocessing

tags_nf = {
    'numero_nota': './/{*}ide/{*}nNF',
    'data_emissao': './/{*}ide/{*}dhEmi'
}

tags_produtos = {
        'CFOP': './/{*}prod/{*}CFOP',
        'Valor Item': './/{*}prod/{*}vProd',
        'Descricao_produto': './/{*}prod/{*}xProd',
        'codigo_item': './/{*}prod/{*}cProd',
    }
def processar_arquivo(arquivo_xml):
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    chv_nfe_tag = root.find('.//{*}infNFe[@Id]')
    chv_nfe = ''
    if chv_nfe_tag:
        chv_nfe = chv_nfe_tag.attrib['Id']

    data_to_save = []

    nnf_data = []
    for tag in tags_nf.values():
        element = root.find(tag)
        value = element.text if element is not None else "Não encontrado"
        nnf_data.append(value)

    for det in root.findall('.//{*}det'):
        num_item = det.attrib['nItem']
        produto_data = [arquivo_xml, chv_nfe, num_item] + nnf_data

        for titulo, tag in tags_produtos.items():

            element = det.find(tag)
            value = element.text if element is not None else "Não encontrado"
            produto_data.append(value)

        data_to_save.append(produto_data)

    return data_to_save

def selecionar_pasta():
    pasta_xml = filedialog.askdirectory(title="Selecionar Pasta com Arquivos XML")
    if pasta_xml:
        processar_arquivos_xml(pasta_xml)



def processar_arquivos_xml(pasta_xml):
    xmls = glob(f'{pasta_xml}/*.xml', recursive=True)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())  # Usa o número de CPUs disponíveis
    results = pool.map(processar_arquivo, xmls)
    pool.close()
    pool.join()

    all_data = [item for sublist in results for item in sublist]  # Aplanha a lista de listas

    column_names = list(tags_nf) + list(tags_produtos)
    column_names.insert(0, 'Número Item')
    column_names.insert(0, 'Chave')
    column_names.insert(0, 'Arquivo')
    df = pd.DataFrame(all_data, columns=column_names)
    df ['Valor Item'] = df['Valor Item'].apply(pd.to_numeric, errors='coerce').fillna(0)
    output_excel = "output.xlsx"
    df.to_excel(output_excel, index=False)
    print(f"Arquivo Excel gerado: {output_excel}")

def main():
    root = tk.Tk()
    root.title("Processamento de Arquivos XML")

    btn_selecionar_pasta = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
    btn_selecionar_pasta.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
