# Definir o caminho do arquivo de entrada e saída
arquivo_entrada = 'TESTE2.txt'
arquivo_saida = 'TESTE2_SCRIPT.txt'

# Ler o arquivo SPED com codificação UTF-8
with open(arquivo_entrada, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Processar as linhas e preencher o campo COD_CTA (9º campo) nos registros D101 e D105
novo_conteudo = []

for linha in linhas:
    if linha.startswith('|D101|') or linha.startswith('|D105|'):
        campos = linha.split('|')
        # Verificar o 9º campo
        if len(campos) > 9 and campos[9] == '':
            campos[9] = '1043'
        linha = '|'.join(campos) + '\n'
    novo_conteudo.append(linha)

# Escrever o novo conteúdo no arquivo de saída com codificação UTF-8
with open(arquivo_saida, 'w', encoding='utf-8') as file:
    file.writelines(novo_conteudo)

print(f"Processamento concluído. O arquivo '{arquivo_saida}' foi gerado.")
