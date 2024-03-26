import os
import glob

def extrair_chaves_saida(arquivo_entrada):
    # Lista para armazenar as chaves de saída
    chaves_saida = []

    print(f"Lendo arquivo: {arquivo_entrada}")

    # Lê o arquivo SPED
    with open(arquivo_entrada, 'r', encoding='latin-1') as f:
        for linha in f:
            # Verifica se a linha contém uma chave de saída
            if linha.startswith('|C100|'):
                campos = linha.split('|')
                if len(campos) >= 13:  # Verifica se há pelo menos 13 campos
                    chave_saida = campos[9]  # A chave de saída está no 9º campo
                    chaves_saida.append(chave_saida.strip())  # Remove espaços em branco e adiciona à lista

    return chaves_saida

def extrair_chaves_saida_pasta(pasta_entrada, arquivo_saida):
    # Lista para armazenar todas as chaves de saída
    todas_chaves_saida = []

    # Lista todos os arquivos na pasta de entrada
    arquivos_sped = glob.glob(os.path.join(pasta_entrada, '*.txt'))

    # Para cada arquivo na pasta
    for arquivo in arquivos_sped:
        # Extrai as chaves de saída do arquivo atual
        chaves_saida = extrair_chaves_saida(arquivo)

        # Adiciona as chaves de saída extraídas à lista geral
        todas_chaves_saida.extend(chaves_saida)

    # Escreve todas as chaves de saída em um arquivo de texto
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for chave in todas_chaves_saida:
            f.write(chave + '\n')

    print(f"As chaves de saída de todos os arquivos SPED foram extraídas e salvas em '{arquivo_saida}'.")

# Pasta de entrada contendo os arquivos SPED
pasta_entrada = 'Z:\\ANE\\ICMS ST\\PROJETO ALTESE\\PROJETO PARA O MA - 072022 A 122023\\BACKUP POR ETAPAS\\DE PARA ITENS CÓD SAÍDA X ENTRADA OK\\ARQUIVOS EFD ICMS IPI COM ITENS OK'

# Arquivo de saída para todas as chaves de saída
arquivo_saida = 'chaves_saida_teste.txt'

# Chama a função para extrair as chaves de saída de todos os arquivos na pasta
extrair_chaves_saida_pasta(pasta_entrada, arquivo_saida)