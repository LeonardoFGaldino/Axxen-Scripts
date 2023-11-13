import os
import zipfile

# Caminho para a pasta contendo os XMLs
caminho_da_pasta = "C:\\Users\\Admin\\Desktop\\ZIPS_TESTE"

# Lista de nomes de arquivo dos XMLs
arquivos_xml = os.listdir(caminho_da_pasta)

# Número de zips que você quer criar
numero_de_zips = 4

# Calcula quantos XMLs serão colocados em cada zip
quantidade_por_zip = len(arquivos_xml) // numero_de_zips

# Loop para criar os zips
for i in range(numero_de_zips):
    # Define o nome do zip
    nome_do_zip = f'arquivos_parte_{i + 1}.zip'

    # Cria um novo zip
    with zipfile.ZipFile(nome_do_zip, 'w') as zip_file:
        # Adiciona os XMLs ao zip
        for arquivo in arquivos_xml[i * quantidade_por_zip: (i + 1) * quantidade_por_zip]:
            caminho_completo = os.path.join(caminho_da_pasta, arquivo)
            zip_file.write(caminho_completo, os.path.basename(caminho_completo))

print("Zips criados com sucesso!")
