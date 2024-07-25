import re
import tkinter as tk
from tkinter import filedialog

# Script 1: Funções de extração e inserção
def extract_0190(input_file_0190):
    with open(input_file_0190, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0190 = [linha for linha in linhas if linha.startswith('|0190|')]
    return registros_0190

def extract_0150(input_file_0150):
    with open(input_file_0150, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0150 = [linha for linha in linhas if linha.startswith('|0150|')]
    return registros_0150

def extract_0500(input_file_0500):
    with open(input_file_0500, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0500 = [linha for linha in linhas if linha.startswith('|0500|')]
    return registros_0500

def insert_0190_after_0150(linhas, registros_0190):
    novo_conteudo = []
    inseriu_0190 = False
    pos_0150 = 0

    for i, linha in enumerate(linhas):
        novo_conteudo.append(linha)
        if linha.startswith('|0150|'):
            pos_0150 = len(novo_conteudo)
        elif linha.startswith('|0200|') and not inseriu_0190:
            novo_conteudo = novo_conteudo[:pos_0150] + registros_0190 + novo_conteudo[pos_0150:]
            inseriu_0190 = True

    if not inseriu_0190:
        novo_conteudo = novo_conteudo[:pos_0150] + registros_0190 + novo_conteudo[pos_0150:]

    return novo_conteudo

def insert_0150_after_0140(linhas, registros_0150):
    novo_conteudo = []
    inseriu_0150 = False
    pos_0140 = 0

    for i, linha in enumerate(linhas):
        novo_conteudo.append(linha)
        if linha.startswith('|0140|'):
            pos_0140 = len(novo_conteudo)
        elif linha.startswith('|0190|') and not inseriu_0150:
            novo_conteudo = novo_conteudo[:pos_0140] + registros_0150 + novo_conteudo[pos_0140:]
            inseriu_0150 = True

    if not inseriu_0150:
        novo_conteudo = novo_conteudo[:pos_0140] + registros_0150 + novo_conteudo[pos_0140:]

    return novo_conteudo

def insert_0500_after_0450(linhas, registros_0500):
    novo_conteudo = []
    inseriu_0500 = False
    pos_0450 = 0

    for i, linha in enumerate(linhas):
        novo_conteudo.append(linha)
        if linha.startswith('|0450|'):
            pos_0450 = len(novo_conteudo)
        elif linha.startswith('|0990|') and not inseriu_0500:
            novo_conteudo = novo_conteudo[:pos_0450] + registros_0500 + novo_conteudo[pos_0450:]
            inseriu_0500 = True

    if not inseriu_0500:
        novo_conteudo = novo_conteudo[:pos_0450] + registros_0500 + novo_conteudo[:pos_0450:]

    return novo_conteudo

def remove_duplicates(linhas):
    records = {"|0200|": set(), "|0190|": set(), "|0150|": set(), "|0500|": set(), "|C100|": set(), "|C170|": set()}
    duplicates = {"|0200|": set(), "|0190|": set(), "|0150|": set(), "|0500|": set(), "|C100|": set(), "|C170|": set()}
    output_lines = []

    for line in linhas:
        record_type = line[:6]
        if record_type in records:
            if line in records[record_type]:
                duplicates[record_type].add(line)
            else:
                records[record_type].add(line)
                output_lines.append(line)
        else:
            output_lines.append(line)

    # Print duplicates
    for record_type, lines in duplicates.items():
        if lines:
            print(f"Duplicated lines for {record_type}:")
            for line in lines:
                print(line)

    return output_lines

def totalizador_0990_9999(linhas):
    count_reg_0 = sum(1 for linha in linhas if linha.startswith('|0'))

    for i, linha in enumerate(linhas):
        if linha.startswith('|0990|'):
            campos = linha.split('|')
            campos[2] = str(count_reg_0)
            linhas[i] = '|'.join(campos)
            break

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

def remove_duplicate_0190(linhas):
    seen = set()
    duplicates = set()
    output_lines = []

    for line in linhas:
        if line.startswith('|0190|'):
            fields = line.split('|')
            second_field = fields[2].lower() if len(fields) > 2 else ''

            if second_field in seen:
                duplicates.add(second_field)
            else:
                seen.add(second_field)
                output_lines.append(line)
        else:
            output_lines.append(line)

    # Print duplicated second fields
    if duplicates:
        print("Duplicated second fields in |0190| records:")
        for duplicate in duplicates:
            print(duplicate)
    else:
        print("No duplicates found for |0190| records.")

    return output_lines

def process_sped_files(input_file, input_file_sped, output_file_sped):
    registros_0190 = extract_0190(input_file)
    registros_0150 = extract_0150(input_file)
    registros_0500 = extract_0500(input_file)

    with open(input_file_sped, 'r', encoding='latin-1') as file:
        linhas = file.readlines()

    novo_conteudo = insert_0150_after_0140(linhas, registros_0150)
    novo_conteudo = insert_0190_after_0150(novo_conteudo, registros_0190)
    novo_conteudo = insert_0500_after_0450(novo_conteudo, registros_0500)

    novo_conteudo = remove_duplicates(novo_conteudo)

    padrao_9900_0150 = re.compile(r'\|9900\|0150\|.+\|')
    encontrou_9900_0150 = False
    for i, linha in enumerate(novo_conteudo):
        if padrao_9900_0150.match(linha):
            encontrou_9900_0150 = True
        if encontrou_9900_0150 and not linha.startswith('|9900|0190|') and not linha.startswith('|9900|'):
            novo_conteudo.insert(i, f'|9900|0190|{len(registros_0190)}|\n')
            break

    for i in range(len(novo_conteudo) - 2, -1, -1):
        if novo_conteudo[i].startswith('|9990|'):
            campos = novo_conteudo[i].split('|')
            campos[2] = str(int(campos[2]) + 1)
            novo_conteudo[i] = '|'.join(campos)
            break

    novo_conteudo = remove_duplicate_0190(novo_conteudo)
    novo_conteudo = totalizador_0990_9999(novo_conteudo)
    novo_conteudo = totalizador_C990(novo_conteudo)

    with open(output_file_sped, 'w', encoding='latin-1') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{output_file_sped}' foi gerado.")

# Script 2: Função para remover duplicatas de |0150|
def remove_duplicate_0150(input_file, output_file):
    codigos_itens = set()
    novo_conteudo = []

    with open(input_file, 'r', encoding='latin-1') as file:
        linhas = file.readlines()

    for linha in linhas:
        if linha.startswith('|0150|'):
            campos = linha.split('|')
            codigo_item = campos[2].lower()
            if codigo_item not in codigos_itens:
                codigos_itens.add(codigo_item)
                novo_conteudo.append(linha)
        else:
            novo_conteudo.append(linha)

    with open(output_file, 'w', encoding='latin-1') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{output_file}' foi gerado.")

# Script 3: Funções de extração e inserção de registros |0150| e atualização de |C100|
def extract_participant_codes(sped_contribuicoes):
    participant_codes = set()
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|C100|') or line.startswith('|D100|') or line.startswith('|A100|'):
                fields = line.split('|')
                participant_code = fields[4]
                participant_codes.add(participant_code)
    return participant_codes

def extract_existing_0150(sped_contribuicoes):
    existing_0150 = set()
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|0150|'):
                fields = line.split('|')
                participant_code = fields[2]
                existing_0150.add(participant_code)
    return existing_0150

def find_0150_in_sped_fiscal(sped_fiscal, participant_codes_needed):
    matching_0150_records = []
    with open(sped_fiscal, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|0150|'):
                fields = line.split('|')
                participant_code = fields[2]
                if participant_code in participant_codes_needed:
                    matching_0150_records.append(line)
    return matching_0150_records

def insert_0150_in_sped_contribuicoes(sped_contribuicoes, matching_0150_records, output_file):
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    new_lines = []
    pos_0150 = 0
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.startswith('|0150|'):
            pos_0150 = len(new_lines)
        if (line.startswith('|C100|') or line.startswith('|D100|') or line.startswith('|A100|')) and matching_0150_records:
            new_lines = new_lines[:pos_0150] + matching_0150_records + new_lines[pos_0150:]
            matching_0150_records = []

    if matching_0150_records:
        new_lines = new_lines[:pos_0150] + matching_0150_records + new_lines[pos_0150:]

    with open(output_file, 'w', encoding='latin-1') as file:
        file.writelines(new_lines)

    print(f"Processamento concluído. O arquivo '{output_file}' foi gerado.")

def extract_cnpj_to_participant_map(sped_contribuicoes_path, sped_fiscal):
    cnpj_to_participant = {}
    for file_path in [sped_contribuicoes_path, sped_fiscal]:
        with open(file_path, 'r', encoding='latin-1') as file:
            for line in file:
                if line.startswith('|0150|'):
                    fields = line.split('|')
                    participant_code = fields[2]
                    cnpj = fields[5]
                    cnpj_to_participant[cnpj] = participant_code
    return cnpj_to_participant

def update_participant_code_in_c100(sped_contribuicoes_path, output_file_path, cnpj_to_participant):
    with open(sped_contribuicoes_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith('|C100|1|0|'):
            fields = line.split('|')
            cnpj = fields[4]
            if cnpj in cnpj_to_participant:
                fields[4] = cnpj_to_participant[cnpj]
                line = '|'.join(fields)
        new_lines.append(line)

    with open(output_file_path, 'w', encoding='latin-1') as file:
        file.writelines(new_lines)

    print(f"Processamento concluído. O arquivo '{output_file_path}' foi atualizado.")

# Script 4: Funções de processamento principal
def process_sped_files_full(input_file, sped_fiscal, intermediate_output, final_output):
    registros_0190 = extract_0190(input_file)
    registros_0150 = extract_0150(input_file)
    registros_0500 = extract_0500(input_file)

    with open(intermediate_output, 'r', encoding='latin-1') as file:
        linhas = file.readlines()

    novo_conteudo = insert_0150_after_0140(linhas, registros_0150)
    novo_conteudo = insert_0190_after_0150(novo_conteudo, registros_0190)
    novo_conteudo = insert_0500_after_0450(novo_conteudo, registros_0500)

    novo_conteudo = remove_duplicates(novo_conteudo)

    padrao_9900_0150 = re.compile(r'\|9900\|0150\|.+\|')
    encontrou_9900_0150 = False
    for i, linha in enumerate(novo_conteudo):
        if padrao_9900_0150.match(linha):
            encontrou_9900_0150 = True
        if encontrou_9900_0150 and not linha.startswith('|9900|0190|') and not linha.startswith('|9900|'):
            novo_conteudo.insert(i, f'|9900|0190|{len(registros_0190)}|\n')
            break

    for i in range(len(novo_conteudo) - 2, -1, -1):
        if novo_conteudo[i].startswith('|9990|'):
            campos = novo_conteudo[i].split('|')
            campos[2] = str(int(campos[2]) + 1)
            novo_conteudo[i] = '|'.join(campos)
            break

    novo_conteudo = remove_duplicate_0190(novo_conteudo)
    novo_conteudo = totalizador_0990_9999(novo_conteudo)
    novo_conteudo = totalizador_C990(novo_conteudo)

    with open(final_output, 'w', encoding='latin-1') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{final_output}' foi gerado.")

# Script 5: Funções adicionais de processamento
def remove_blank_lines(lines):
    return [line for line in lines if line.strip('|').strip()]

def process_file(input_file_path, output_file_path):
    codigo_analitico_compras = "34000020000000005"
    codigo_analitico_vendas = "90200010000000005"

    with open(input_file_path, 'r', encoding='latin-1') as file:
        linhas = file.readlines()

    novo_conteudo = []
    codigo_atual = ""

    for linha in linhas:
        if linha.startswith('|C100|'):
            campos = linha.split('|')
            ind_oper = campos[2]
            if ind_oper == '0':
                codigo_atual = codigo_analitico_compras
            elif ind_oper == '1':
                codigo_atual = codigo_analitico_vendas

        if linha.startswith('|C170|'):
            campos = linha.split('|')
            while len(campos) <= 37:
                campos.append('')
            campos[37] = codigo_atual if campos[37].strip() == '' else campos[37]
            linha = '|'.join(campos[:38]).strip() + '|\n'

        novo_conteudo.append(linha)

    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|D101|') or linha.startswith('|D105|'):
            campos = linha.split('|')
            if len(campos) > 9 and campos[9] == '':
                campos[9] = '1043'
            novo_conteudo[i] = '|'.join(campos)

    for i, linha in enumerate(novo_conteudo):
        if linha.startswith('|D101|') or linha.startswith('|D105|'):
            campos = linha.split('|')
            if campos[2] == '':
                campos[2] = '9'
            novo_conteudo[i] = '|'.join(campos)

    codigos_itens = set()
    linhas_sem_duplicatas = []

    for linha in novo_conteudo:
        if linha.startswith('|0150|'):
            campos = linha.split('|')
            codigo_item = campos[2].lower()
            if codigo_item not in codigos_itens:
                codigos_itens.add(codigo_item)
                linhas_sem_duplicatas.append(linha)
        else:
            linhas_sem_duplicatas.append(linha)

    linhas_sem_duplicatas = remove_blank_lines(linhas_sem_duplicatas)
    linhas_sem_duplicatas = update_totals(linhas_sem_duplicatas)
    linhas_sem_duplicatas = totalizador_C990(linhas_sem_duplicatas)

    with open(output_file_path, 'w', encoding='latin-1') as file:
        file.writelines(linhas_sem_duplicatas)

    print(f"Processamento concluído. O arquivo '{output_file_path}' foi atualizado.")

# Atualizar totalizadores e registros adicionais
def update_totals(linhas):
    count_reg_0 = sum(1 for linha in linhas if linha.startswith('|0'))

    for i, linha in enumerate(linhas):
        if linha.startswith('|0990|'):
            campos = linha.split('|')
            campos[2] = str(count_reg_0)
            linhas[i] = '|'.join(campos)
            break

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

# Fluxo principal do script combinado
def main():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(title="Selecione o arquivo sped_contribuicoes.txt", filetypes=[("Arquivos de texto", "*.txt")])
    sped_fiscal = filedialog.askopenfilename(title="Selecione o arquivo sped_fiscal.txt", filetypes=[("Arquivos de texto", "*.txt")])
    intermediate_output = filedialog.asksaveasfilename(title="Selecione o arquivo de saída intermediário para salvar", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    final_output = filedialog.asksaveasfilename(title="Selecione o arquivo de saída final para salvar", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])

    if input_file and sped_fiscal and intermediate_output and final_output:
        # Processar arquivos SPED
        process_sped_files(input_file, input_file, intermediate_output)
        # Remover duplicatas de |0150|
        remove_duplicate_0150(intermediate_output, intermediate_output)
        # Processar e atualizar registros de |0150| e |C100|
        process_sped_files_full(intermediate_output, sped_fiscal, intermediate_output, final_output)
        # Processar arquivos adicionais
        process_file(final_output, final_output)
        print(f"Resultados exportados para {intermediate_output} e {final_output}")
    else:
        print("Seleção de arquivos inválida.")

if __name__ == "__main__":
    main()
