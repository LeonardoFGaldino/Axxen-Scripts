import os
import re


caminho_da_pasta = "C:\\Users\\Admin\\Desktop\\SPED C100"


pasta_destino = "C:\\Users\\Admin\\Desktop\\SPED FINAL"


padrao_c100 = re.compile(r'\|C100\|0\|')


def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()

    linhas_modificadas = []
    for linha in linhas:
        if padrao_c100.search(linha):
            partes = linha.split('|')
            cfop = partes[11]
            if cfop not in ('5102', '1102', '1403', '2102', '2403'):
                linha = linha[:25] + linha[25:].replace('|50|', '|53|', 1)
        linhas_modificadas.append(linha)

    nome_arquivo = os.path.basename(caminho_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_arquivo)

    with open(caminho_destino, 'w', encoding='utf-8') as arquivo_destino:
        arquivo_destino.writelines(linhas_modificadas)


for arquivo in os.listdir(caminho_da_pasta):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(caminho_da_pasta, arquivo)
        processar_arquivo(caminho_arquivo)

print("Processamento concluído.")
