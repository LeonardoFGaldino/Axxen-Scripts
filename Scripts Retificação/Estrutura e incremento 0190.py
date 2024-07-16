import re

def extract_0190(input_file_0190):
    """Extrai todos os registros 0190 de um arquivo de entrada."""
    with open(input_file_0190, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    registros_0190 = [linha for linha in linhas if linha.startswith('|0190|')]
    return registros_0190

def insert_0190_after_0150(input_file_sped, output_file_sped, registros_0190):
    """Insere registros 0190 após o último registro 0150 e antes do primeiro registro 0200 em um arquivo SPED."""
    with open(input_file_sped, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    novo_conteudo = []
    inseriu_0190 = False
    pos_0150 = 0
    count_reg_0 = 0

    for i, linha in enumerate(linhas):
        novo_conteudo.append(linha)
        if linha.startswith('|0150|'):
            # Marcar a posição após o último registro 0150
            pos_0150 = len(novo_conteudo)
        elif linha.startswith('|0200|') and not inseriu_0190:
            # Inserir registros 0190 após o último registro 0150 e antes do primeiro registro 0200
            novo_conteudo = novo_conteudo[:pos_0150] + registros_0190 + novo_conteudo[pos_0150:]
            inseriu_0190 = True
        # Contar registros que começam com "0"
        if linha.startswith('|0'):
            count_reg_0 += 1

    # Se não encontrou nenhum registro 0200, adicionar os registros 0190 no final do bloco 0150
    if not inseriu_0190:
        novo_conteudo = novo_conteudo[:pos_0150] + registros_0190 + novo_conteudo[pos_0150:]

    # Atualizar o registro 0990 com a nova contagem de registros que começam com "0"
    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|0990|'):
            count_reg_0 += len(registros_0190)  # Adicionar registros 0190 à contagem
            campos = linha.split('|')
            campos[2] = str(count_reg_0)
            novo_conteudo[i] = '|'.join(campos)
            break

    # Adicionar a linha |9900|0190|X| logo após |9900|0150|?
    '''
    se precisar adicionar linha no totalizador. (quando não tiver o registro no sped e for adicionado pela primeira vez)
    
    '''
    padrao_9900_0150 = re.compile(r'\|9900\|0150\|.+\|')
    encontrou_9900_0150 = False
    for i, linha in enumerate(novo_conteudo):
        if padrao_9900_0150.match(linha):
            encontrou_9900_0150 = True
        if encontrou_9900_0150 and not linha.startswith('|9900|0190|') and not linha.startswith('|9900|'):
            novo_conteudo.insert(i, f'|9900|0190|{len(registros_0190)}|\n')
            break

    # Incrementar a penúltima linha |9990|X|
    for i in range(len(novo_conteudo) - 2, -1, -1):
        if novo_conteudo[i].startswith('|9990|'):
            campos = novo_conteudo[i].split('|')
            campos[2] = str(int(campos[2]) + 1)
            novo_conteudo[i] = '|'.join(campos)
            break

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
input_file_0190 = 'sped_contribuicoes_202204.txt'
input_file_sped = 'sped_contribuicoes_202205.txt'
output_file_sped = 'arquivo_destino_com_0190_atualizado.txt'

# Extrair registros 0190
registros_0190 = extract_0190(input_file_0190)

# Inserir registros 0190 no arquivo de destino
insert_0190_after_0150(input_file_sped, output_file_sped, registros_0190)
