import os
import xml.etree.ElementTree as ET
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from glob import glob
import multiprocessing


def selecionar_pasta():
    pasta_xml = filedialog.askdirectory(title="Selecionar Pasta com Arquivos XML")
    if pasta_xml:
        processar_arquivos_xml(pasta_xml)

pasta_xml = "C:\\Users\\Admin\\Downloads\\Arquivosxml"

tags_para_buscar = {
    'CFOP': './/{*}CFOP',
    'Descricao_produto': './/{*}xProd',
    'codigo_item': './/{*}cProd',
    'numero_nota': './/{*}nNF',
    'data_emissao': './/{*}dhEmi'
}

def processar_arquivos_xml(pasta_xml):
    all_data = []
    xmls = glob(f'{pasta_xml}/*.xml', recursive=True)
    for arquivo_xml in xmls:

        if arquivo_xml.endswith(".xml"):
            tree = ET.parse(arquivo_xml)
            root = tree.getroot()

            chv_nfe_tag = root.find('.//{*}infNFe[@Id]')

            chv_nfe = ''
            if chv_nfe_tag:
                chv_nfe = chv_nfe_tag.attrib['Id']

            data_to_save = [arquivo_xml, chv_nfe]

            for tag, xpath in tags_para_buscar.items():
                element = root.find(xpath)
                valor = element.text if element is not None else "Não encontrado"
                data_to_save.append(valor)
            all_data.append(data_to_save)

    column_names = list(tags_para_buscar.keys())
    column_names.insert(0, 'Chave')
    column_names.insert(0, 'Arquivo')
    df = pd.DataFrame(all_data, columns=column_names)

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
