'''

SCRIPT PRONTO

'''

# import pandas as pd
# import os
#
# # Função para substituir valores nas posições exatas, ajustando zeros à esquerda se necessário
# def substituir_valor_por_posicao(linha, valor_novo, inicio, fim):
#     tamanho_campo = fim - inicio + 1
#     if len(valor_novo) > tamanho_campo:
#         raise ValueError(f"O valor '{valor_novo}' excede o tamanho permitido de {tamanho_campo} caracteres.")
#     valor_ajustado = valor_novo.zfill(tamanho_campo)
#     # Ajuste dos índices para indexação baseada em zero
#     inicio_index = inicio - 1
#     fim_index = fim  # Em slicing, o índice final é exclusivo
#     return linha[:inicio_index] + valor_ajustado + linha[fim_index:]
#
# # Função para encontrar números de linha contendo um padrão específico
# def encontrar_linhas_por_padrao(content, padrao):
#     linhas_encontradas = []
#     for idx, linha in enumerate(content):
#         if padrao in linha:
#             linhas_encontradas.append(idx)
#     return linhas_encontradas
#
# # Função para obter as posições de PIS e COFINS com base no tamanho do valor e tipo de arquivo
# def obter_posicoes_pis(len_pis, tipo_arquivo):
#     if tipo_arquivo == "RETIF":
#         if len_pis <= 7:
#             posicoes = [
#                 (None, 75, 84),  # Primeira posição
#                 (None, 165, 177)  # Segunda posição
#             ]
#         elif len_pis == 8:
#             posicoes = [
#                 (None, 75, 84),
#                 (None, 168, 177)
#             ]
#         elif len_pis == 9:
#             posicoes = [
#                 (None, 74, 85),
#                 (None, 167, 178)
#             ]
#         else:
#             raise ValueError(f"O valor PIS tem um tamanho não suportado.")
#     elif tipo_arquivo == "ORIGI":
#         if len_pis <= 7:
#             posicoes = [
#                 (None, 77, 84),
#                 (None, 170, 177)
#             ]
#         elif len_pis == 8:
#             posicoes = [
#                 (None, 76, 84),
#                 (None, 169, 177)
#             ]
#         elif len_pis == 9:
#             posicoes = [
#                 (None, 75, 84),
#                 (None, 168, 177)
#             ]
#         else:
#             raise ValueError(f"O valor PIS tem um tamanho não suportado.")
#     else:
#         raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
#     return posicoes
#
# def obter_posicoes_cofins(len_cofins, tipo_arquivo):
#     if tipo_arquivo == "RETIF":
#         if len_cofins <= 8:
#             posicoes = [
#                 (None, 74, 84),
#                 (None, 167, 177)
#             ]
#         elif len_cofins == 9:
#             posicoes = [
#                 (None, 74, 85),
#                 (None, 167, 178)
#             ]
#         else:
#             raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
#     elif tipo_arquivo == "ORIGI":
#         if len_cofins <= 8:
#             posicoes = [
#                 (None, 77, 84),
#                 (None, 170, 177)
#             ]
#         elif len_cofins == 9:
#             posicoes = [
#                 (None, 76, 84),
#                 (None, 169, 177)
#             ]
#         else:
#             raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
#     else:
#         raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
#     return posicoes
#
# # Função para substituir os recibos nas posições corretas
# def inserir_recibo(content, recibo):
#     posicoes_recibo = [
#         (2, 42, 53)  # Linha 2, Colunas 42 a 53
#     ]
#     for (linha_idx, inicio, fim) in posicoes_recibo:
#         linha_atual = content[linha_idx - 1]
#         content[linha_idx - 1] = substituir_valor_por_posicao(linha_atual, recibo, inicio, fim)
#     return content
#
# # Função para converter o período de "MMYYYY" para "YYYYMM"
# def converter_periodo(periodo):
#     periodo = periodo.strip()
#     if len(periodo) == 6:
#         mes = periodo[:2]
#         ano = periodo[2:]
#         return ano + mes  # Retorna no formato "YYYYMM"
#     else:
#         return periodo  # Retorna como está se não tiver 6 caracteres
#
# # Caminhos para o arquivo Excel e pasta de arquivos de texto
# excel_file_path = "C:\\Users\\Axxen\\Downloads\\Modelo_DCTF.xlsx"  # Substitua pelo caminho real
# txt_folder_path = "C:\\Users\\Axxen\\Desktop\\LANSA DEC\\bok"  # Pasta contendo os arquivos .txt
# output_folder_path = 'C:\\Users\\Axxen\\Desktop\\teste dctf\\arquivos_processados2'  # Pasta para salvar os arquivos modificados
#
# # Lendo a planilha Excel
# df = pd.read_excel(excel_file_path, converters={'PERÍODO': str})
#
# # Garantindo que a coluna 'PERÍODO' é string e removendo espaços em branco
# df['PERÍODO'] = df['PERÍODO'].astype(str).str.strip()
#
# # Convertendo o período na planilha de "MMYYYY" para "YYYYMM"
# df['PERÍODO'] = df['PERÍODO'].apply(converter_periodo)
#
# # Criando a pasta de saída se não existir
# if not os.path.exists(output_folder_path):
#     os.makedirs(output_folder_path)
#
# # Listando todos os arquivos .txt na pasta especificada
# for filename in os.listdir(txt_folder_path):
#     if filename.endswith(".txt"):
#         txt_file_path = os.path.join(txt_folder_path, filename)
#         print(f"Processando arquivo: {filename}")
#
#         # Extraindo o período e tipo do nome do arquivo
#         parts = filename.split('-')
#         if len(parts) >= 3:
#             periodo_txt = parts[2]
#             tipo_arquivo = "RETIF" if "RETIF" in filename else "ORIGI" if "ORIGI" in filename else None
#         else:
#             print(f"Nome de arquivo '{filename}' não está no formato esperado.")
#             continue
#
#         if not tipo_arquivo:
#             print(f"Tipo de arquivo não identificado para '{filename}'.")
#             continue
#
#         # Procurando o período correspondente na planilha
#         row = df[df['PERÍODO'] == periodo_txt]
#
#         if not row.empty:
#             pis_novo = row.iloc[0]['PIS FINAL']
#             cofins_novo = row.iloc[0]['COFINS FINAL']
#             recibo = row.iloc[0]['RECIBOS DCTF']
#         else:
#             print(f"Período '{periodo_txt}' não encontrado na planilha Excel para o arquivo '{filename}'.")
#             continue
#
#         # Processando os valores de PIS, COFINS e recibo (removendo caracteres indesejados)
#         def processar_valor(valor):
#             return ''.join(filter(str.isdigit, str(valor)))
#
#         pis_novo = processar_valor(pis_novo)
#         cofins_novo = processar_valor(cofins_novo)
#         recibo = processar_valor(recibo)
#
#         # Lendo o conteúdo do arquivo de texto
#         with open(txt_file_path, 'r') as file:
#             content = file.readlines()
#
#         # Encontrando as linhas que contêm PIS e COFINS
#         pis_line_numbers = encontrar_linhas_por_padrao(content, "6691201M")
#         cofins_line_numbers = encontrar_linhas_por_padrao(content, "7585601M")
#
#         # Obter o tamanho dos valores
#         len_pis = len(pis_novo)
#         len_cofins = len(cofins_novo)
#
#         # Obter as posições para PIS e COFINS
#         posicoes_pis = obter_posicoes_pis(len_pis, tipo_arquivo)
#         posicoes_cofins = obter_posicoes_cofins(len_cofins, tipo_arquivo)
#
#         # Substituindo os valores de PIS
#         for idx, linha_idx in enumerate(pis_line_numbers):
#             if idx >= len(posicoes_pis):
#                 print(f"Mais linhas de PIS encontradas do que posições definidas para o arquivo '{filename}'.")
#                 break
#             inicio_pis, fim_pis = posicoes_pis[idx][1], posicoes_pis[idx][2]
#             linha_atual = content[linha_idx]
#             content[linha_idx] = substituir_valor_por_posicao(linha_atual, pis_novo, inicio_pis, fim_pis)
#
#         # Substituindo os valores de COFINS
#         for idx, linha_idx in enumerate(cofins_line_numbers):
#             if idx >= len(posicoes_cofins):
#                 print(f"Mais linhas de COFINS encontradas do que posições definidas para o arquivo '{filename}'.")
#                 break
#             inicio_cofins, fim_cofins = posicoes_cofins[idx][1], posicoes_cofins[idx][2]
#             linha_atual = content[linha_idx]
#             content[linha_idx] = substituir_valor_por_posicao(linha_atual, cofins_novo, inicio_cofins, fim_cofins)
#
#         # Inserindo os recibos nas posições corretas
#         content = inserir_recibo(content, recibo)
#
#         # Salvando o arquivo com as modificações
#         output_file_path = os.path.join(output_folder_path, filename)
#         with open(output_file_path, 'w') as file:
#             file.writelines(content)
#
#         print(f"Arquivo '{filename}' salvo em: {output_file_path}")
#
# print("Processamento concluído.")



'''

SCRIPT PRONTO PULANDO PROCESSO DE DOIS CODIGOS

'''


# import pandas as pd
# import os
#
# # Função para substituir valores nas posições exatas, ajustando zeros à esquerda se necessário
# def substituir_valor_por_posicao(linha, valor_novo, inicio, fim):
#     tamanho_campo = fim - inicio + 1
#     if len(valor_novo) > tamanho_campo:
#         raise ValueError(f"O valor '{valor_novo}' excede o tamanho permitido de {tamanho_campo} caracteres.")
#     valor_ajustado = valor_novo.zfill(tamanho_campo)
#     # Ajuste dos índices para indexação baseada em zero
#     inicio_index = inicio - 1
#     fim_index = fim  # Em slicing, o índice final é exclusivo
#     return linha[:inicio_index] + valor_ajustado + linha[fim_index:]
#
# # Função para encontrar números de linha contendo um padrão específico
# def encontrar_linhas_por_padrao(content, padrao):
#     linhas_encontradas = []
#     for idx, linha in enumerate(content):
#         if padrao in linha:
#             linhas_encontradas.append(idx)
#     return linhas_encontradas
#
# # Função para obter as posições de PIS e COFINS com base no tamanho do valor e tipo de arquivo
# def obter_posicoes_pis(len_pis, tipo_arquivo):
#     if tipo_arquivo == "RETIF":
#         if len_pis <= 7:
#             posicoes = [
#                 (None, 75, 84),  # Primeira posição
#                 (None, 165, 177)  # Segunda posição
#             ]
#         elif len_pis == 8:
#             posicoes = [
#                 (None, 75, 84),
#                 (None, 168, 177)
#             ]
#         elif len_pis == 9:
#             posicoes = [
#                 (None, 74, 85),
#                 (None, 167, 178)
#             ]
#         else:
#             raise ValueError(f"O valor PIS tem um tamanho não suportado.")
#     elif tipo_arquivo == "ORIGI":
#         if len_pis <= 7:
#             posicoes = [
#                 (None, 77, 84),
#                 (None, 170, 177)
#             ]
#         elif len_pis == 8:
#             posicoes = [
#                 (None, 76, 84),
#                 (None, 169, 177)
#             ]
#         elif len_pis == 9:
#             posicoes = [
#                 (None, 75, 84),
#                 (None, 168, 177)
#             ]
#         else:
#             raise ValueError(f"O valor PIS tem um tamanho não suportado.")
#     else:
#         raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
#     return posicoes
#
# def obter_posicoes_cofins(len_cofins, tipo_arquivo):
#     if tipo_arquivo == "RETIF":
#         if len_cofins <= 8:
#             posicoes = [
#                 (None, 74, 84),
#                 (None, 167, 177)
#             ]
#         elif len_cofins == 9:
#             posicoes = [
#                 (None, 74, 85),
#                 (None, 167, 178)
#             ]
#         else:
#             raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
#     elif tipo_arquivo == "ORIGI":
#         if len_cofins <= 8:
#             posicoes = [
#                 (None, 77, 84),
#                 (None, 170, 177)
#             ]
#         elif len_cofins == 9:
#             posicoes = [
#                 (None, 76, 84),
#                 (None, 169, 177)
#             ]
#         else:
#             raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
#     else:
#         raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
#     return posicoes
#
# # Função para substituir os recibos nas posições corretas
# def inserir_recibo(content, recibo):
#     posicoes_recibo = [
#         (2, 42, 53)  # Linha 2, Colunas 42 a 53
#     ]
#     for (linha_idx, inicio, fim) in posicoes_recibo:
#         linha_atual = content[linha_idx - 1]
#         content[linha_idx - 1] = substituir_valor_por_posicao(linha_atual, recibo, inicio, fim)
#     return content
#
# # Função para converter o período de "MMYYYY" para "YYYYMM"
# def converter_periodo(periodo):
#     periodo = periodo.strip()
#     if len(periodo) == 6:
#         mes = periodo[:2]
#         ano = periodo[2:]
#         return ano + mes  # Retorna no formato "YYYYMM"
#     else:
#         return periodo  # Retorna como está se não tiver 6 caracteres
#
# # Caminhos para o arquivo Excel e pasta de arquivos de texto
# excel_file_path = "C:\\Users\\Axxen\\Downloads\\Modelo_DCTF.xlsx"  # Substitua pelo caminho real
# txt_folder_path = "C:\\Users\\Axxen\\Desktop\\LANSA DEC\\bok"  # Pasta contendo os arquivos .txt
# output_folder_path = 'C:\\Users\\Axxen\\Desktop\\teste dctf\\arquivos_processados2'  # Pasta para salvar os arquivos modificados
#
# # Lendo a planilha Excel
# df = pd.read_excel(excel_file_path, converters={'PERÍODO': str})
#
# # Garantindo que a coluna 'PERÍODO' é string e removendo espaços em branco
# df['PERÍODO'] = df['PERÍODO'].astype(str).str.strip()
#
# # Convertendo o período na planilha de "MMYYYY" para "YYYYMM"
# df['PERÍODO'] = df['PERÍODO'].apply(converter_periodo)
#
# # Criando a pasta de saída se não existir
# if not os.path.exists(output_folder_path):
#     os.makedirs(output_folder_path)
#
# # Listando todos os arquivos .txt na pasta especificada
# for filename in os.listdir(txt_folder_path):
#     if filename.endswith(".txt"):
#         txt_file_path = os.path.join(txt_folder_path, filename)
#         print(f"Processando arquivo: {filename}")
#
#         # Extraindo o período e tipo do nome do arquivo
#         parts = filename.split('-')
#         if len(parts) >= 3:
#             periodo_txt = parts[2]
#             tipo_arquivo = "RETIF" if "RETIF" in filename else "ORIGI" if "ORIGI" in filename else None
#         else:
#             print(f"Nome de arquivo '{filename}' não está no formato esperado.")
#             continue
#
#         if not tipo_arquivo:
#             print(f"Tipo de arquivo não identificado para '{filename}'.")
#             continue
#
#         # Lendo o conteúdo do arquivo de texto
#         with open(txt_file_path, 'r') as file:
#             content = file.readlines()
#
#         # Verificando se há linhas R11 repetidas exatamente iguais e consecutivas
#         encontrou_repeticao = False
#         for idx in range(len(content) - 1):
#             linha_atual = content[idx].strip()
#             linha_proxima = content[idx + 1].strip()
#             if linha_atual.startswith('R11') and linha_proxima.startswith('R11'):
#                 if linha_atual == linha_proxima:
#                     print(f"Arquivo '{filename}' possui linhas R11 repetidas. Pulando este arquivo.")
#                     encontrou_repeticao = True
#                     break
#
#         if encontrou_repeticao:
#             continue  # Pula para o próximo arquivo
#
#         # Procurando o período correspondente na planilha
#         row = df[df['PERÍODO'] == periodo_txt]
#
#         if not row.empty:
#             pis_novo = row.iloc[0]['PIS FINAL']
#             cofins_novo = row.iloc[0]['COFINS FINAL']
#             recibo = row.iloc[0]['RECIBOS DCTF']
#         else:
#             print(f"Período '{periodo_txt}' não encontrado na planilha Excel para o arquivo '{filename}'.")
#             continue
#
#         # Processando os valores de PIS, COFINS e recibo (removendo caracteres indesejados)
#         def processar_valor(valor):
#             return ''.join(filter(str.isdigit, str(valor)))
#
#         pis_novo = processar_valor(pis_novo)
#         cofins_novo = processar_valor(cofins_novo)
#         recibo = processar_valor(recibo)
#
#         # Encontrando as linhas que contêm PIS e COFINS
#         pis_line_numbers = encontrar_linhas_por_padrao(content, "6691201M")
#         cofins_line_numbers = encontrar_linhas_por_padrao(content, "7585601M")
#
#         # Obter o tamanho dos valores
#         len_pis = len(pis_novo)
#         len_cofins = len(cofins_novo)
#
#         # Obter as posições para PIS e COFINS
#         posicoes_pis = obter_posicoes_pis(len_pis, tipo_arquivo)
#         posicoes_cofins = obter_posicoes_cofins(len_cofins, tipo_arquivo)
#
#         # Substituindo os valores de PIS
#         for idx, linha_idx in enumerate(pis_line_numbers):
#             if idx >= len(posicoes_pis):
#                 print(f"Mais linhas de PIS encontradas do que posições definidas para o arquivo '{filename}'.")
#                 break
#             inicio_pis, fim_pis = posicoes_pis[idx][1], posicoes_pis[idx][2]
#             linha_atual = content[linha_idx]
#             content[linha_idx] = substituir_valor_por_posicao(linha_atual, pis_novo, inicio_pis, fim_pis)
#
#         # Substituindo os valores de COFINS
#         for idx, linha_idx in enumerate(cofins_line_numbers):
#             if idx >= len(posicoes_cofins):
#                 print(f"Mais linhas de COFINS encontradas do que posições definidas para o arquivo '{filename}'.")
#                 break
#             inicio_cofins, fim_cofins = posicoes_cofins[idx][1], posicoes_cofins[idx][2]
#             linha_atual = content[linha_idx]
#             content[linha_idx] = substituir_valor_por_posicao(linha_atual, cofins_novo, inicio_cofins, fim_cofins)
#
#         # Inserindo os recibos nas posições corretas
#         content = inserir_recibo(content, recibo)
#
#         # Salvando o arquivo com as modificações
#         output_file_path = os.path.join(output_folder_path, filename)
#         with open(output_file_path, 'w') as file:
#             file.writelines(content)
#
#         print(f"Arquivo '{filename}' salvo em: {output_file_path}")
#
# print("Processamento concluído.")



'''

SCRIPT PRONTO PULANDO PROCESSO DE DOIS CODIGOS E PULANDO PROCESSO 0 OU VAZIO

'''

import pandas as pd
import os

# Função para substituir valores nas posições exatas, ajustando zeros à esquerda se necessário
def substituir_valor_por_posicao(linha, valor_novo, inicio, fim):
    tamanho_campo = fim - inicio + 1
    if len(valor_novo) > tamanho_campo:
        raise ValueError(f"O valor '{valor_novo}' excede o tamanho permitido de {tamanho_campo} caracteres.")
    valor_ajustado = valor_novo.zfill(tamanho_campo)
    # Ajuste dos índices para indexação baseada em zero
    inicio_index = inicio - 1
    fim_index = fim  # Em slicing, o índice final é exclusivo
    return linha[:inicio_index] + valor_ajustado + linha[fim_index:]

# Função para encontrar números de linha contendo um padrão específico
def encontrar_linhas_por_padrao(content, padrao):
    linhas_encontradas = []
    for idx, linha in enumerate(content):
        if padrao in linha:
            linhas_encontradas.append(idx)
    return linhas_encontradas

# Função para obter as posições de PIS e COFINS com base no tamanho do valor e tipo de arquivo
def obter_posicoes_pis(len_pis, tipo_arquivo):
    if tipo_arquivo == "RETIF":
        if len_pis <= 7:
            posicoes = [
                (None, 75, 84),  # Primeira posição
                (None, 165, 177)  # Segunda posição
            ]
        elif len_pis == 8:
            posicoes = [
                (None, 75, 84),
                (None, 168, 177)
            ]
        elif len_pis == 9:
            posicoes = [
                (None, 74, 85),
                (None, 167, 178)
            ]
        else:
            raise ValueError(f"O valor PIS tem um tamanho não suportado.")
    elif tipo_arquivo == "ORIGI":
        if len_pis <= 7:
            posicoes = [
                (None, 77, 84),
                (None, 170, 177)
            ]
        elif len_pis == 8:
            posicoes = [
                (None, 76, 84),
                (None, 169, 177)
            ]
        elif len_pis == 9:
            posicoes = [
                (None, 75, 84),
                (None, 168, 177)
            ]
        else:
            raise ValueError(f"O valor PIS tem um tamanho não suportado.")
    else:
        raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
    return posicoes

def obter_posicoes_cofins(len_cofins, tipo_arquivo):
    if tipo_arquivo == "RETIF":
        if len_cofins <= 8:
            posicoes = [
                (None, 74, 84),
                (None, 167, 177)
            ]
        elif len_cofins == 9:
            posicoes = [
                (None, 74, 85),
                (None, 167, 178)
            ]
        else:
            raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
    elif tipo_arquivo == "ORIGI":
        if len_cofins <= 8:
            posicoes = [
                (None, 77, 84),
                (None, 170, 177)
            ]
        elif len_cofins == 9:
            posicoes = [
                (None, 76, 84),
                (None, 169, 177)
            ]
        else:
            raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
    else:
        raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
    return posicoes

# Função para substituir os recibos nas posições corretas
def inserir_recibo(content, recibo):
    posicoes_recibo = [
        (2, 42, 53)  # Linha 2, Colunas 42 a 53
    ]
    for (linha_idx, inicio, fim) in posicoes_recibo:
        linha_atual = content[linha_idx - 1]
        content[linha_idx - 1] = substituir_valor_por_posicao(linha_atual, recibo, inicio, fim)
    return content

# Função para converter o período de "MMYYYY" para "YYYYMM"
def converter_periodo(periodo):
    periodo = periodo.strip()
    if len(periodo) == 6:
        mes = periodo[:2]
        ano = periodo[2:]
        return ano + mes  # Retorna no formato "YYYYMM"
    else:
        return periodo  # Retorna como está se não tiver 6 caracteres

# Caminhos para o arquivo Excel e pasta de arquivos de texto
excel_file_path = "C:\\Users\\Axxen\\Desktop\\teste dctf\\Planilha de preenchimento DCTF.xlsx" # Substitua pelo caminho real
#excel_file_path = "C:\\Users\\Axxen\\Downloads\\Modelo_DCTF.xlsx"
txt_folder_path = "C:\\Users\\Axxen\\Desktop\\LANSA DEC\\bok"  # Pasta contendo os arquivos .txt
output_folder_path = 'C:\\Users\\Axxen\\Desktop\\teste dctf\\arquivos_processados2'  # Pasta para salvar os arquivos modificados

# Lendo a planilha Excel
df = pd.read_excel(excel_file_path, converters={'PERÍODO': str})

# Garantindo que a coluna 'PERÍODO' é string e removendo espaços em branco
df['PERÍODO'] = df['PERÍODO'].astype(str).str.strip()

# Convertendo o período na planilha de "MMYYYY" para "YYYYMM"
df['PERÍODO'] = df['PERÍODO'].apply(converter_periodo)

# Criando a pasta de saída se não existir
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Listando todos os arquivos .txt na pasta especificada
for filename in os.listdir(txt_folder_path):
    if filename.endswith(".txt"):
        txt_file_path = os.path.join(txt_folder_path, filename)
        print(f"Processando arquivo: {filename}")

        # Extraindo o período e tipo do nome do arquivo
        parts = filename.split('-')
        if len(parts) >= 3:
            periodo_txt = parts[2]
            tipo_arquivo = "RETIF" if "RETIF" in filename else "ORIGI" if "ORIGI" in filename else None
        else:
            print(f"Nome de arquivo '{filename}' não está no formato esperado.")
            continue

        if not tipo_arquivo:
            print(f"Tipo de arquivo não identificado para '{filename}'.")
            continue

        # Lendo o conteúdo do arquivo de texto
        with open(txt_file_path, 'r') as file:
            content = file.readlines()

        # Verificando se há linhas R11 repetidas exatamente iguais e consecutivas
        encontrou_repeticao = False
        for idx in range(len(content) - 1):
            linha_atual = content[idx].strip()
            linha_proxima = content[idx + 1].strip()
            if linha_atual.startswith('R11') and linha_proxima.startswith('R11'):
                if linha_atual == linha_proxima:
                    print(f"Arquivo '{filename}' possui linhas R11 repetidas. Pulando este arquivo.")
                    encontrou_repeticao = True
                    break

        if encontrou_repeticao:
            continue  # Pula para o próximo arquivo

        # Procurando o período correspondente na planilha
        row = df[df['PERÍODO'] == periodo_txt]

        if not row.empty:
            pis_novo = row.iloc[0]['PIS FINAL']
            cofins_novo = row.iloc[0]['COFINS FINAL']
            recibo = row.iloc[0]['RECIBO']

            # Se o PIS ou COFINS for "0" ou estiver vazio, pule o processamento deste arquivo
            if not pis_novo or pis_novo == "0" or not cofins_novo or cofins_novo == "0":
                print(f"PIS ou COFINS é '0' ou vazio para o período '{periodo_txt}' no arquivo '{filename}'. Pulando este arquivo.")
                continue
        else:
            print(f"Período '{periodo_txt}' não encontrado na planilha Excel para o arquivo '{filename}'.")
            continue

        # Processando os valores de PIS, COFINS e recibo (removendo caracteres indesejados)
        def processar_valor(valor):
            return ''.join(filter(str.isdigit, str(valor)))

        pis_novo = processar_valor(pis_novo)
        cofins_novo = processar_valor(cofins_novo)
        recibo = processar_valor(recibo)

        # Encontrando as linhas que contêm PIS e COFINS
        pis_line_numbers = encontrar_linhas_por_padrao(content, "6691201M")
        cofins_line_numbers = encontrar_linhas_por_padrao(content, "7585601M")

        # Obter o tamanho dos valores
        len_pis = len(pis_novo)
        len_cofins = len(cofins_novo)

        # Obter as posições para PIS e COFINS
        posicoes_pis = obter_posicoes_pis(len_pis, tipo_arquivo)
        posicoes_cofins = obter_posicoes_cofins(len_cofins, tipo_arquivo)

        # Substituindo os valores de PIS
        for idx, linha_idx in enumerate(pis_line_numbers):
            if idx >= len(posicoes_pis):
                print(f"Mais linhas de PIS encontradas do que posições definidas para o arquivo '{filename}'.")
                break
            inicio_pis, fim_pis = posicoes_pis[idx][1], posicoes_pis[idx][2]
            linha_atual = content[linha_idx]
            content[linha_idx] = substituir_valor_por_posicao(linha_atual, pis_novo, inicio_pis, fim_pis)

        # Substituindo os valores de COFINS
        for idx, linha_idx in enumerate(cofins_line_numbers):
            if idx >= len(posicoes_cofins):
                print(f"Mais linhas de COFINS encontradas do que posições definidas para o arquivo '{filename}'.")
                break
            inicio_cofins, fim_cofins = posicoes_cofins[idx][1], posicoes_cofins[idx][2]
            linha_atual = content[linha_idx]
            content[linha_idx] = substituir_valor_por_posicao(linha_atual, cofins_novo, inicio_cofins, fim_cofins)

        # Inserindo os recibos nas posições corretas
        content = inserir_recibo(content, recibo)

        # Salvando o arquivo com as modificações
        output_file_path = os.path.join(output_folder_path, filename)
        with open(output_file_path, 'w') as file:
            file.writelines(content)

        print(f"Arquivo '{filename}' salvo em: {output_file_path}")

print("Processamento concluído.")





