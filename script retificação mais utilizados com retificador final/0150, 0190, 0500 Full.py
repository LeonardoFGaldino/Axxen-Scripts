import re
import tkinter as tk
from tkinter import filedialog

def extract_0190(input_file_0190):
    """Extrai todos os registros 0190 de um arquivo de entrada."""
    with open(input_file_0190, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0190 = [linha for linha in linhas if linha.startswith('|0190|')]
    return registros_0190

def extract_0150(input_file_0150):
    """Extrai todos os registros 0150 de um arquivo de entrada."""
    with open(input_file_0150, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0150 = [linha for linha in linhas if linha.startswith('|0150|')]
    return registros_0150

def extract_0500(input_file_0500):
    """Extrai todos os registros 0500 de um arquivo de entrada."""
    with open(input_file_0500, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    registros_0500 = [linha for linha in linhas if linha.startswith('|0500|')]
    return registros_0500

def insert_0190_after_0150(linhas, registros_0190):
    """Insere registros 0190 após o último registro 0150 e antes do primeiro registro 0200 em um arquivo SPED."""
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
    """Insere registros 0150 após o último registro 0140 e antes do primeiro registro 0190 em um arquivo SPED."""
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
    """Insere registros 0500 após o último registro 0450 e antes do registro 0990 em um arquivo SPED."""
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
        novo_conteudo = novo_conteudo[:pos_0450] + registros_0500 + novo_conteudo[pos_0450:]

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
    novo_conteudo = update_totals(novo_conteudo)
    novo_conteudo = totalizador_C990(novo_conteudo)



    with open(output_file_sped, 'w', encoding='latin-1') as file:
        file.writelines(novo_conteudo)

    print(f"Processamento concluído. O arquivo '{output_file_sped}' foi gerado.")

def main():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(title="Selecione o arquivo sped_contribuicoes_202209.txt", filetypes=[("Arquivos de texto", "*.txt")])
    input_file_sped = filedialog.askopenfilename(title="Selecione o arquivo sped_contribuicoes_202208_atualizado2.txt", filetypes=[("Arquivos de texto", "*.txt")])
    output_file_sped = filedialog.asksaveasfilename(title="Selecione o arquivo sped_contribuicoes_202208_atualizado3.txt para salvar", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])

    if input_file and input_file_sped and output_file_sped:
        process_sped_files(input_file, input_file_sped, output_file_sped)
        print(f"Resultados exportados para {output_file_sped}")
    else:
        print("Seleção de arquivos inválida.")

if __name__ == "__main__":
    main()
