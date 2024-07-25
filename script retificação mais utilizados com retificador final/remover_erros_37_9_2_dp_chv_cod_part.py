import re
from tkinter import filedialog
import tkinter as tk


def remove_blank_lines(lines):
    # Filtra as linhas, removendo qualquer linha que esteja completamente vazia ou que contenha apenas delimitadores
    return [line for line in lines if line.strip('|').strip()]

def process_file(input_file_path, output_file_path):
    # Defina os códigos analíticos contábeis para compras e vendas
    codigo_analitico_compras = "34000020000000005"
    codigo_analitico_vendas = "90200010000000005"

    # Ler o arquivo SPED com codificação 'latin-1'
    with open(input_file_path, 'r', encoding='latin-1') as file:
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

    # Processar as linhas e preencher o campo COD_CTA (9º campo) nos registros D101 e D105
    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|D101|') or linha.startswith('|D105|'):
            campos = linha.split('|')
            # Verificar o 9º campo
            if len(campos) > 9 and campos[9] == '':
                campos[9] = '1043'
            novo_conteudo[i] = '|'.join(campos)

    # Processar as linhas e adicionar o número 9 no 2º campo nos registros D101 e D105 se estiver vazio
    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|D101|') or linha.startswith('|D105|'):
            campos = linha.split('|')
            # Verificar se o 2º campo está vazio
            if campos[2] == '':
                campos[2] = '9'
            novo_conteudo[i] = '|'.join(campos)

    # Conjunto para manter os códigos únicos dos itens
    codigos_itens = set()
    linhas_sem_duplicatas = []

    # Lista para armazenar o novo conteúdo sem duplicidades
    for linha in novo_conteudo:
        if linha.startswith('|0150|'):
            campos = linha.split('|')
            codigo_item = campos[2].lower()  # Normalizar para minúsculas
            # Verificar se o código do item já foi visto
            if codigo_item not in codigos_itens:
                # Adicionar o código do item ao conjunto
                codigos_itens.add(codigo_item)
                # Adicionar a linha ao novo conteúdo
                linhas_sem_duplicatas.append(linha)
        else:
            # Adicionar todas as outras linhas que não são 0200
            linhas_sem_duplicatas.append(linha)

    # Remover linhas em branco ou que contêm apenas delimitadores
    linhas_sem_duplicatas = remove_blank_lines(linhas_sem_duplicatas)

    # Atualizar totalizadores e registros adicionais
    linhas_sem_duplicatas = update_totals(linhas_sem_duplicatas)
    linhas_sem_duplicatas = totalizador_C990(linhas_sem_duplicatas)


    # Escrever o novo conteúdo no arquivo de saída com codificação 'latin-1'
    with open(output_file_path, 'w', encoding='latin-1') as file:
        file.writelines(linhas_sem_duplicatas)

    print(f"Processamento concluído. O arquivo '{output_file_path}' foi atualizado.")


def update_totals(linhas):
    count_reg_0 = sum(1 for linha in linhas if linha.startswith('|0'))

    # Atualizar o registro 0990 com a nova contagem de registros que começam com "0"
    for i, linha in enumerate(linhas):
        if linha.startswith('|0990|'):
            campos = linha.split('|')
            campos[2] = str(count_reg_0)
            linhas[i] = '|'.join(campos)
            break

    # Atualizar o registro 9999 com o novo total de linhas
    total_linhas = len(linhas)
    for i, linha in enumerate(linhas):
        if linha.startswith('|9999|'):
            campos = linha.split('|')
            campos[2] = str(total_linhas)
            linhas[i] = '|'.join(campos)
            break

    return linhas

def totalizador_C990(linhas):
    count_reg_C = sum(1 for linha in linhas if linha.startswith('|C'))

    for i, linha in enumerate(linhas):
        if linha.startswith('|C990|'):
            campos = linha.split('|')
            campos[2] = str(count_reg_C)
            linhas[i] = '|'.join(campos)
            break

    return linhas


def main():
    root = tk.Tk()
    root.withdraw()

    # Selecionar os três arquivos .txt
    input_file_sped = filedialog.askopenfilename(title="Selecione o arquivo sped_contribuicoes_202208_atualizado2.txt", filetypes=[("Arquivos de texto", "*.txt")])
    output_file_sped = filedialog.asksaveasfilename(title="Selecione o arquivo sped_contribuicoes_202208_atualizado3.txt para salvar", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])

    if input_file_sped and output_file_sped:
        # Chamar a função de processamento com os caminhos dos arquivos .txt selecionados
        process_file(input_file_sped, output_file_sped)
        print(f"Resultados exportados para {output_file_sped}")
    else:
        print("Seleção de arquivos inválida.")

if __name__ == "__main__":
    main()



# # Caminhos dos arquivos de entrada e saída
# input_file_path = 'sped_contribuicoes_202208_atualizado.txt'  # Nome do arquivo de entrada
# output_file_path = 'sped_contribuicoes_202208_atualizado2.txt'  # Nome do arquivo de saída após a remoção das linhas em branco e atualização dos códigos
#
# process_file(input_file_path, output_file_path)
