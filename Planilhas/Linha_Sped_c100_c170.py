import pandas as pd
from openpyxl import load_workbook

# Caminho do arquivo
arquivo_path = "C:\\Users\\Axxen\\Desktop\\SCRIPT LEO\\tarefa\\PLANILHA_MODELO_REVENDA.xlsx"

# Carregar os dados da planilha
df = pd.read_excel(arquivo_path, sheet_name='REVENDA', header=1, dtype=str)

# Dicionário para armazenar as relações pai (C100) - filhos (C170)
c100_c170_dict = {}

# Variável para armazenar o registro C100 atual
c100_atual = None

# Percorrer cada linha do DataFrame original
for index, row in df.iterrows():
    c100 = row['C100']  # Coluna C100
    c170 = row['C170']  # Coluna C170

    if pd.notna(c100):  # Se a linha contém um registro C100
        c100_atual = c100
        if c100_atual not in c100_c170_dict:
            c100_c170_dict[c100_atual] = []  # Inicializar a lista de filhos para esse C100

    if pd.notna(c170):  # Se a linha contém um registro C170
        if c100_atual:  # Garantir que existe um C100 associado
            c100_c170_dict[c100_atual].append(c170)  # Adicionar o C170 à lista de filhos desse C100

# Lista para armazenar os registros na ordem correta
linhas_sped = []

# Construir a lista final na ordem correta, pai seguido dos filhos
for c100, c170_list in c100_c170_dict.items():
    linhas_sped.append(c100)  # Adicionar o pai (C100)
    linhas_sped.extend(c170_list)  # Adicionar todos os filhos (C170) associados a esse pai

# Criar um novo DataFrame exclusivamente com a coluna 'LINHA SPED'
df_linha_sped = pd.DataFrame({'LINHA SPED': linhas_sped})

# Escrever os dados na planilha, substituindo a aba existente se necessário
with pd.ExcelWriter(arquivo_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_linha_sped.to_excel(writer, sheet_name='LINHA_SPED_REVENDA', index=False)

print("A estrutura pai-filho foi criada com sucesso na planilha 'LINHA_SPED'.")
