# Definir o caminho do arquivo de entrada e saída
arquivo_entrada = '2024_02_ATUALIZADO_script.txt'
arquivo_saida = '2024_02_ATUALIZADO_script2.txt'

# Ler o arquivo SPED com codificação UTF-8
with open(arquivo_entrada, 'r', encoding='latin-1') as file:
    linhas = file.readlines()

# Conjunto para manter os códigos únicos dos itens
codigos_itens = set()

# Lista para armazenar o novo conteúdo sem duplicidades
novo_conteudo = []

for linha in linhas:
    if linha.startswith('|0150|'):
        campos = linha.split('|')
        codigo_item = campos[2].lower()  # Normalizar para minúsculas
        # Verificar se o código do item já foi visto
        if codigo_item not in codigos_itens:
            # Adicionar o código do item ao conjunto
            codigos_itens.add(codigo_item)
            # Adicionar a linha ao novo conteúdo
            novo_conteudo.append(linha)
        # Se o código do item já foi visto, não adicionar a linha (remover duplicidade)
    else:
        # Adicionar todas as outras linhas que não são 0200
        novo_conteudo.append(linha)

# Escrever o novo conteúdo no arquivo de saída com codificação UTF-8
with open(arquivo_saida, 'w', encoding='latin-1') as file:
    file.writelines(novo_conteudo)

print(f"Processamento concluído. O arquivo '{arquivo_saida}' foi gerado.")