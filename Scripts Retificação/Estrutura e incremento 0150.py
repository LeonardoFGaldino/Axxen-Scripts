import re

def extract_0150(input_file_0150):
    """Extrai todos os registros 0150 de um arquivo de entrada."""
    with open(input_file_0150, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    registros_0150 = [linha for linha in linhas if linha.startswith('|0150|')]
    return registros_0150

# def remove_duplicates(records):
#     """Remove duplicatas mantendo a ordem."""
#     seen = set()
#     unique_records = []
#     for record in records:
#         if record not in seen:
#             unique_records.append(record)
#             seen.add(record)
#     return unique_records

def insert_0150_after_0140(input_file_sped, output_file_sped, registros_0150):
    """Insere registros 0150 após o último registro 0140 e antes do primeiro registro 0190 em um arquivo SPED."""
    with open(input_file_sped, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    novo_conteudo = []
    inseriu_0150 = False
    pos_0140 = 0
    count_reg_0 = 0

    # registros_0150 = remove_duplicates(registros_0150)  # Remove duplicatas dos registros 0150

    for i, linha in enumerate(linhas):
        novo_conteudo.append(linha)
        if linha.startswith('|0140|'):
            # Marcar a posição após o último registro 0140
            pos_0140 = len(novo_conteudo)
        elif linha.startswith('|0190|') and not inseriu_0150:
            # Inserir registros 0150 após o último registro 0140 e antes do primeiro registro 0190
            novo_conteudo = novo_conteudo[:pos_0140] + registros_0150 + novo_conteudo[pos_0140:]
            inseriu_0150 = True
        # Contar registros que começam com "0"
        if linha.startswith('|0'):
            count_reg_0 += 1

    # Se não encontrou nenhum registro 0190, adicionar os registros 0150 no final do bloco 0140
    if not inseriu_0150:
        novo_conteudo = novo_conteudo[:pos_0140] + registros_0150 + novo_conteudo[pos_0140:]


    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|0990|'):
            count_reg_0 += len(registros_0150)  # Adicionar registros 0190 à contagem
            campos = linha.split('|')
            campos[2] = str(count_reg_0)
            novo_conteudo[i] = '|'.join(campos)
            break

        # # Adicionar a linha |9900|0190|X| logo após |9900|0150|?

    '''
      se precisar adicionar linha no totalizador. (quando não tiver o registro no sped e for adicionado pela primeira vez)
    
    '''

    # padrao_9900_0150 = re.compile(r'\|9900\|0150\|.+\|')
    # encontrou_9900_0150 = False
    # for i, linha in enumerate(novo_conteudo):
    #     if padrao_9900_0150.match(linha):
    #         encontrou_9900_0150 = True
    #     if encontrou_9900_0150 and not linha.startswith('|9900|0190|') and not linha.startswith('|9900|'):
    #         novo_conteudo.insert(i, f'|9900|0190|{len(registros_0190)}|\n')
    #         break

    # Incrementar a penúltima linha |9990|X|
    # for i in range(len(novo_conteudo) - 2, -1, -1):
    #     if novo_conteudo[i].startswith('|9990|'):
    #         campos = novo_conteudo[i].split('|')
    #         campos[2] = str(int(campos[2]) + 1)
    #         novo_conteudo[i] = '|'.join(campos)
    #         break

    # Atualizar o registro 9999 com o novo total de linhas
    total_linhas = len(novo_conteudo)
    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|9999|'):
            campos = linha.split('|')
            campos[2] = str(total_linhas)
            novo_conteudo[i] = '|'.join(campos)
            break

    with open(output_file_sped, 'w', encoding='utf-8') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{output_file_sped}' foi gerado.")

# Caminhos dos arquivos de entrada e saída
input_file_0150 = 'sped_contribuicoes_202203.txt'
input_file_sped = 'sped_contribuicoes_202204.txt'
output_file_sped = 'arquivo_destino_com_0150_atualizadoooo2.txt'

# Extrair registros 0150
registros_0150 = extract_0150(input_file_0150)

# Inserir registros 0150 no arquivo de destino
insert_0150_after_0140(input_file_sped, output_file_sped, registros_0150)
