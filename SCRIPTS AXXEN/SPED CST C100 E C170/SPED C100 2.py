import os

caminho_da_pasta = "C:\\Users\\Admin\\Desktop\\SPED C100"
pasta_destino = "C:\\Users\\Admin\\Desktop\\SPED FINAL"


cfops_permitidos = ['5102', '1102', '1403', '2102', '2403']

def processar_linha(linha):
    partes = linha.strip('|').split('|')
    if len(partes) > 24 and partes[1] == 'C170':
        cfop = partes[11]
        if cfop not in cfops_permitidos:
            partes[24] = '53'
        return '|'.join(partes) + '|'
    return linha

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()

    linhas_modificadas = [processar_linha(linha) for linha in linhas]

    nome_arquivo = os.path.basename(caminho_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_arquivo)

    with open(caminho_destino, 'w', encoding='latin-1') as arquivo_destino:
        arquivo_destino.writelines(linhas_modificadas)

for arquivo in os.listdir(caminho_da_pasta):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(caminho_da_pasta, arquivo)
        processar_arquivo(caminho_arquivo)

print("Processamento concluído.")

N