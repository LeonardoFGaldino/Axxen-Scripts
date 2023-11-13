import os


caminho_da_pasta = "C:\\Users\\Admin\\Desktop\\SPED C100"


pasta_destino = "C:\\Users\\Admin\\Desktop\\SPED FINAL"


cfops_permitidos = ['5102', '1102', '1403', '2102', '2403']


def processar_linha(linha):
    partes = linha.strip().strip('|').split('|')
    if len(partes) > 25:
        cfop = partes[11]
        if cfop not in cfops_permitidos:
            partes[24] = '51'
            partes[30] = '51'
    return '|' + '|'.join(partes) + '|\n'


def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()

    nota_de_entrada = False
    linhas_modificadas = []

    for linha in linhas:
        if linha.startswith('|C100|'):
            ind_oper = linha[6]
            if ind_oper == '0':
                nota_de_entrada = True
            else:
                nota_de_entrada = False

        if linha.startswith('|C170|') and nota_de_entrada:
            linha = processar_linha(linha)

        linhas_modificadas.append(linha)

    ##linhas_modificadas = [processar_linha(linha) for linha in linhas if '|C170|' in linha]

    nome_arquivo = os.path.basename(caminho_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_arquivo)

    with open(caminho_destino, 'w', encoding='latin-1') as arquivo_destino:
        arquivo_destino.writelines(linhas_modificadas)


for arquivo in os.listdir(caminho_da_pasta):
    if arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(caminho_da_pasta, arquivo)
        processar_arquivo(caminho_arquivo)


