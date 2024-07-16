import re

def remove_blank_lines(lines):
    # Filtra as linhas, removendo qualquer linha que esteja completamente vazia ou que contenha apenas delimitadores
    return [line for line in lines if line.strip('|').strip()]

def process_file(input_file_path, output_file_path):
    # Defina os códigos analíticos contábeis para compras e vendas
    codigo_analitico_compras = "34000020000000005"
    codigo_analitico_vendas = "90200010000000005"

    # Ler o arquivo SPED com codificação UTF-8
    with open(input_file_path, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    # Processar as linhas e preencher o campo COD_CTA no registro C170
    novo_conteudo = []
    codigo_atual = ""

    for linha in linhas:
        if linha.startswith('|C100|'):
            # Verificar o valor do campo IND_OPER (entrada ou saída)
            campos = linha.split('|')
            ind_oper = campos[2]
            if ind_oper == '0':
                codigo_atual = codigo_analitico_compras
            elif ind_oper == '1':
                codigo_atual = codigo_analitico_vendas

        if linha.startswith('|C170|'):
            # Preencher o campo COD_CTA se estiver vazio
            campos = linha.split('|')
            # Adiciona código analítico contábil como 37º campo
            while len(campos) <= 37:
                campos.append('')
            campos[37] = codigo_atual if campos[37].strip() == '' else campos[37]
            linha = '|'.join(campos[:38]).strip() + '|\n'  # Ajusta para remover qualquer espaço extra no final

        novo_conteudo.append(linha)

    # Remover linhas em branco ou que contêm apenas delimitadores
    novo_conteudo = remove_blank_lines(novo_conteudo)

    # Escrever o novo conteúdo no arquivo de saída com codificação UTF-8
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{output_file_path}' foi atualizado.")

# Exemplo de uso
input_file_path = '2021_09_ATUALIZADO3.txt'  # Nome do arquivo de entrada
output_file_path = '2021_09_ATUALIZADO3_atualizado.txt'  # Nome do arquivo de saída após a remoção das linhas em branco e atualização dos códigos

process_file(input_file_path, output_file_path)
