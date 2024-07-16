# Definir o caminho do arquivo de entrada e saída
arquivo_entrada = '2021_09_CST_PIS.txt'
arquivo_saida = 'seu_arquivo_sped_corrigido.txt'

# Ler o arquivo SPED com codificação UTF-8
with open(arquivo_entrada, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Processar as linhas e corrigir o campo CST_PIS (25º campo) no registro C170
novo_conteudo = []

for linha in linhas:
    if linha.startswith('|C170|'):
        campos = linha.split('|')
        # Verificar o campo CST_PIS (25º campo)
        if len(campos) > 25 and (campos[25] == '0' or campos[25] == ''):
            campos[25] = '53'
        linha = '|'.join(campos) + '\n'
    novo_conteudo.append(linha)

# Escrever o novo conteúdo no arquivo de saída com codificação UTF-8
with open(arquivo_saida, 'w', encoding='utf-8') as file:
    file.writelines(novo_conteudo)

print(f"Processamento concluído. O arquivo '{arquivo_saida}' foi gerado.")
