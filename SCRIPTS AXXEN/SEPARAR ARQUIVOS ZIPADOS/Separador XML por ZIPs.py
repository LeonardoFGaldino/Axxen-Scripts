import os
import zipfile
from concurrent.futures import ThreadPoolExecutor

# Caminho para a pasta contendo os XMLs
caminho_da_pasta = "Z:\\Teste\\XMLTAGS"

# Lista de nomes de arquivo dos XMLs
arquivos_xml = os.listdir(caminho_da_pasta)

# Número de zips que você quer criar
numero_de_zips = 2

# Calcula quantos XMLs serão colocados em cada zip
quantidade_por_zip = len(arquivos_xml) // numero_de_zips

def criar_zip(nome_do_zip, arquivos):
    with zipfile.ZipFile(nome_do_zip, 'w') as zip_file:
        for arquivo in arquivos:
            caminho_completo = os.path.join(caminho_da_pasta, arquivo)
            zip_file.write(caminho_completo, os.path.basename(caminho_completo))
    print(f"Zip {nome_do_zip} criado com sucesso!")

# Criação de threads usando ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    for i in range(numero_de_zips):
        nome_do_zip = f'arquivos_parte_{i + 1}.zip'
        arquivos = arquivos_xml[i * quantidade_por_zip: (i + 1) * quantidade_por_zip]
        executor.submit(criar_zip, nome_do_zip, arquivos)

print("Zips criados com sucesso!")
