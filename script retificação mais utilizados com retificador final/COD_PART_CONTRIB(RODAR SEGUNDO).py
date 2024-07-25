import re

# Funções para extração e inserção de registros |0150|

def extract_participant_codes(sped_contribuicoes):
    """Extrai todos os códigos dos participantes dos registros C100, D100 e A100 de um arquivo de entrada."""
    participant_codes = set()
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|C100|') or line.startswith('|D100|') or line.startswith('|A100|'):
                fields = line.split('|')
                participant_code = fields[4]
                participant_codes.add(participant_code)
    return participant_codes

def extract_existing_0150(sped_contribuicoes):
    """Extrai todos os códigos dos participantes do registro 0150 de um arquivo de entrada."""
    existing_0150 = set()
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|0150|'):
                fields = line.split('|')
                participant_code = fields[2]
                existing_0150.add(participant_code)
    return existing_0150

def find_0150_in_sped_fiscal(sped_fiscal, participant_codes_needed):
    """Encontra os registros 0150 correspondentes no arquivo sped_fiscal.txt."""
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
    """Insere registros 0150 no arquivo sped_contribuicoes na hierarquia correta."""
    with open(sped_contribuicoes, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    # Inserir novos registros 0150 após o último registro 0140 e antes do primeiro registro 0190
    new_lines = []
    pos_0150 = 0
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.startswith('|0150|'):
            pos_0150 = len(new_lines)
        if (line.startswith('|C100|') or line.startswith('|D100|') or line.startswith('|A100|')) and matching_0150_records:
            new_lines = new_lines[:pos_0150] + matching_0150_records + new_lines[pos_0150:]
            matching_0150_records = []  # Clear the records to avoid adding them multiple times

    # Add remaining matching_0150_records if any (e.g., if no |C100|, |D100|, or |A100| records found)
    if matching_0150_records:
        new_lines = new_lines[:pos_0150] + matching_0150_records + new_lines[pos_0150:]

    with open(output_file, 'w', encoding='latin-1') as file:
        file.writelines(new_lines)

    print(f"Processamento concluído. O arquivo '{output_file}' foi gerado.")

# Funções para substituição de CNPJ por código de participante nos registros |C100|

def extract_cnpj_to_participant_map(sped_contribuicoes_path):
    """Cria um mapa de CNPJ para o código do participante a partir do arquivo sped_contribuicoes.txt."""
    cnpj_to_participant = {}
    with open(sped_contribuicoes_path, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith('|0150|'):
                fields = line.split('|')
                participant_code = fields[2]
                cnpj = fields[5]
                cnpj_to_participant[cnpj] = participant_code
    return cnpj_to_participant

def update_participant_code_in_c100(sped_contribuicoes_path, output_file_path, cnpj_to_participant):
    """Substitui o CNPJ pelo código do participante nos registros C100."""
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



# Fluxo principal do script combinado

def main():
    # Caminhos dos arquivos de entrada e saída
    sped_contribuicoes = '2024_02_ATUALIZADO_script3.txt'
    sped_fiscal = 'sped_02_2024.txt'
    intermediate_output = 'sped_contribuicoes_intermediario.txt'
    final_output = '2024_02_ATUALIZADO_script4.txt'

    # Extrair códigos dos participantes dos registros C100, D100 e A100
    participant_codes = extract_participant_codes(sped_contribuicoes)

    # Extrair códigos dos participantes já existentes no registro 0150 do sped_contribuicoes
    existing_0150 = extract_existing_0150(sped_contribuicoes)

    # Encontrar códigos dos participantes que precisam ser adicionados
    participant_codes_needed = participant_codes - existing_0150

    # Buscar registros 0150 correspondentes no sped_fiscal
    matching_0150_records = find_0150_in_sped_fiscal(sped_fiscal, participant_codes_needed)

    # Inserir registros 0150 no sped_contribuicoes
    insert_0150_in_sped_contribuicoes(sped_contribuicoes, matching_0150_records, intermediate_output)

    # Criar mapa de CNPJ para código do participante
    cnpj_to_participant = extract_cnpj_to_participant_map(intermediate_output)

    # Atualizar códigos dos participantes nos registros C100
    update_participant_code_in_c100(intermediate_output, final_output, cnpj_to_participant)

if __name__ == "__main__":
    main()
