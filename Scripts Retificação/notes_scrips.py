def extract_0190(input_file_0190):
    """Extrai todos os registros 0190 de um arquivo de entrada."""
    with open(input_file_0190, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    registros_0190 = [linha for linha in linhas if linha.startswith('|0190|')]
    return registros_0190





'''
depois que o 0190 foi adicionado, precisamos modificar algumas linhas:
siga essa ordem:

1° erro 2-QTD_LIN-0

valor esperado: 1633
conteúdo do campo: 1571
registro: 0990

o 0190 foi adicionado então teremos que acrescentar a quantidade que foi adicionada no 0990 

ele fica nessa posição:
|0500|01012021|04|A|6|93902010000000006|RECUPERACOES DIVERSAS|3.01.01.05.01.99||
|0990|1633|
|A001|0|

2° erro 1-REG

é necessário totalizar os registros do tipo 0190 no bloco 9 registro 9999

adicione uma linha examente igual a essa: "|9900|0190|1|" logo depois da linha |9900|0150||

3° some + 1 no 2° campo na penultima linha do sped, exemplo:
 
antes: |9990|58|
depois |9990|59|

isso por que foi criado anteriormente no bloco 9.

erro final: 2-QTD_LIN totalizador de linhas registro 9999

deve conter o total de linhas

exemplo ultima linha do sped no 2° campo:

|9999|10273|

--------------------------------------------------------------------------------------
COD_PART registro 0150 

exemplo da linha do sped, apenas para:

|D100|0|1|FOR000000088|57|00|001||611665|41220400428307001321570010006116651006116650|07042022|07042022|0||46,3|0|0|46,3|0|0|46,3|23|1043|

copiar 0150 de um sped.txt e colar em outro.

posição do 0150: fica depois do |0140| e antes do |0190|

use essa mesma logica:

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









































'''

