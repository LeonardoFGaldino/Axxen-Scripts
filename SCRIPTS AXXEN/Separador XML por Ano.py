import os
import shutil
from datetime import datetime
import xml.etree.ElementTree as ET


caminho_da_pasta = "C:\\Users\\Admin\\Desktop\\ZIPS_TESTE"


arquivos_xml = os.listdir(caminho_da_pasta)



def extrair_ano(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ano_elemento = root.find('ano')
    if ano_elemento is not None:
        return ano_elemento.text
    else:

        return str(datetime.fromtimestamp(os.path.getctime(xml_path)).year)



for arquivo_xml in arquivos_xml:
    caminho_completo = os.path.join(caminho_da_pasta, arquivo_xml)
    ano = extrair_ano(caminho_completo)
    pasta_ano = os.path.join(caminho_da_pasta, ano)


    if not os.path.exists(pasta_ano):
        os.makedirs(pasta_ano)

    
    shutil.move(caminho_completo, os.path.join(pasta_ano, arquivo_xml))

print("XMLs organizados por ano com sucesso!")
