import tkinter as tk
from tkinter import filedialog
from tkinter import Label, PhotoImage
import pandas as pd
import os

# Funções auxiliares
def substituir_valor_por_posicao(linha, valor_novo, inicio, fim):
    tamanho_campo = fim - inicio + 1
    if len(valor_novo) > tamanho_campo:
        raise ValueError(f"O valor '{valor_novo}' excede o tamanho permitido de {tamanho_campo} caracteres.")
    valor_ajustado = valor_novo.zfill(tamanho_campo)
    inicio_index = inicio - 1
    fim_index = fim
    return linha[:inicio_index] + valor_ajustado + linha[fim_index:]

def encontrar_linhas_por_padrao(content, padrao):
    linhas_encontradas = []
    for idx, linha in enumerate(content):
        if padrao in linha:
            linhas_encontradas.append(idx)
    return linhas_encontradas

def obter_posicoes_pis(len_pis, tipo_arquivo):
    if tipo_arquivo == "RETIF":
        if len_pis <= 7:
            posicoes = [(None, 75, 84), (None, 165, 177)]
        elif len_pis == 8:
            posicoes = [(None, 75, 84), (None, 168, 177)]
        elif len_pis == 9:
            posicoes = [(None, 74, 85), (None, 167, 178)]
        else:
            raise ValueError(f"O valor PIS tem um tamanho não suportado.")
    elif tipo_arquivo == "ORIGI":
        if len_pis <= 7:
            posicoes = [(None, 77, 84), (None, 170, 177)]
        elif len_pis == 8:
            posicoes = [(None, 76, 84), (None, 169, 177)]
        elif len_pis == 9:
            posicoes = [(None, 75, 84), (None, 168, 177)]
        else:
            raise ValueError(f"O valor PIS tem um tamanho não suportado.")
    else:
        raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
    return posicoes

def obter_posicoes_cofins(len_cofins, tipo_arquivo):
    if tipo_arquivo == "RETIF":
        if len_cofins <= 8:
            posicoes = [(None, 74, 84), (None, 167, 177)]
        elif len_cofins == 9:
            posicoes = [(None, 74, 85), (None, 167, 178)]
        else:
            raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
    elif tipo_arquivo == "ORIGI":
        if len_cofins <= 8:
            posicoes = [(None, 77, 84), (None, 170, 177)]
        elif len_cofins == 9:
            posicoes = [(None, 76, 84), (None, 169, 177)]
        else:
            raise ValueError(f"O valor COFINS tem um tamanho não suportado.")
    else:
        raise ValueError(f"Tipo de arquivo '{tipo_arquivo}' não suportado.")
    return posicoes

def inserir_recibo(content, recibo):
    posicoes_recibo = [(2, 42, 53)]
    for (linha_idx, inicio, fim) in posicoes_recibo:
        linha_atual = content[linha_idx - 1]
        content[linha_idx - 1] = substituir_valor_por_posicao(linha_atual, recibo, inicio, fim)
    return content

def converter_periodo(periodo):
    periodo = periodo.strip()
    if len(periodo) == 6:
        mes = periodo[:2]
        ano = periodo[2:]
        return ano + mes
    else:
        return periodo

# Função principal
def iniciar_extracao():
    excel_file_path = excel_entry.get()
    txt_folder_path = pasta_entry.get()
    output_folder_path = output_entry.get()

    if not os.path.isfile(excel_file_path):
        resultado_label.config(text="Arquivo Excel inválido.")
        return
    if not os.path.isdir(txt_folder_path):
        resultado_label.config(text="Pasta de entrada inválida.")
        return
    if not os.path.isdir(output_folder_path):
        try:
            os.makedirs(output_folder_path)
        except Exception as e:
            resultado_label.config(text="Pasta de saída inválida.")
            return

    try:
        df = pd.read_excel(excel_file_path, converters={'PERÍODO': str})
        df['PERÍODO'] = df['PERÍODO'].astype(str).str.strip()
        df['PERÍODO'] = df['PERÍODO'].apply(converter_periodo)

        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        for filename in os.listdir(txt_folder_path):
            if filename.endswith(".txt"):
                txt_file_path = os.path.join(txt_folder_path, filename)
                print(f"Processando arquivo: {filename}")

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

                with open(txt_file_path, 'r') as file:
                    content = file.readlines()

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
                    continue

                row = df[df['PERÍODO'] == periodo_txt]

                if not row.empty:
                    pis_novo = row.iloc[0]['PIS FINAL']
                    cofins_novo = row.iloc[0]['COFINS FINAL']
                    recibo = row.iloc[0]['RECIBO']

                    if not pis_novo or pis_novo == "0" or not cofins_novo or cofins_novo == "0":
                        print(f"PIS ou COFINS é '0' ou vazio para o período '{periodo_txt}' no arquivo '{filename}'. Pulando este arquivo.")
                        continue
                else:
                    print(f"Período '{periodo_txt}' não encontrado na planilha Excel para o arquivo '{filename}'.")
                    continue

                def processar_valor(valor):
                    return ''.join(filter(str.isdigit, str(valor)))

                pis_novo = processar_valor(pis_novo)
                cofins_novo = processar_valor(cofins_novo)
                recibo = processar_valor(recibo)

                pis_line_numbers = encontrar_linhas_por_padrao(content, "6691201M")
                cofins_line_numbers = encontrar_linhas_por_padrao(content, "7585601M")

                len_pis = len(pis_novo)
                len_cofins = len(cofins_novo)

                posicoes_pis = obter_posicoes_pis(len_pis, tipo_arquivo)
                posicoes_cofins = obter_posicoes_cofins(len_cofins, tipo_arquivo)

                for idx, linha_idx in enumerate(pis_line_numbers):
                    if idx >= len(posicoes_pis):
                        print(f"Mais linhas de PIS encontradas do que posições definidas para o arquivo '{filename}'.")
                        break
                    inicio_pis, fim_pis = posicoes_pis[idx][1], posicoes_pis[idx][2]
                    linha_atual = content[linha_idx]
                    content[linha_idx] = substituir_valor_por_posicao(linha_atual, pis_novo, inicio_pis, fim_pis)

                for idx, linha_idx in enumerate(cofins_line_numbers):
                    if idx >= len(posicoes_cofins):
                        print(f"Mais linhas de COFINS encontradas do que posições definidas para o arquivo '{filename}'.")
                        break
                    inicio_cofins, fim_cofins = posicoes_cofins[idx][1], posicoes_cofins[idx][2]
                    linha_atual = content[linha_idx]
                    content[linha_idx] = substituir_valor_por_posicao(linha_atual, cofins_novo, inicio_cofins, fim_cofins)

                content = inserir_recibo(content, recibo)

                output_file_path = os.path.join(output_folder_path, filename)
                with open(output_file_path, 'w') as file:
                    file.writelines(content)

                print(f"Arquivo '{filename}' salvo em: {output_file_path}")

        print("Processamento concluído.")
        resultado_label.config(text="Processamento concluído.")
    except Exception as e:
        print("Ocorreu um erro:", str(e))
        resultado_label.config(text="Ocorreu um erro: " + str(e))

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Processamento de Arquivos DCTF")
root.configure(bg="#333333")

nome_programa2 = tk.Label(root, text="Script DCTF", font=("Roboto", 30), bg="#333333", fg="white")
instrucoes_label = tk.Label(root, text="Informe os diretórios e o arquivo Excel:", font=("Roboto", 15), bg="#333333", fg="white")

# Pasta de entrada
pasta_label = tk.Label(root, text="Pasta com arquivos .txt não selecionada.", font=("Roboto", 10), bg="#333333", fg="white")
pasta_entry = tk.Entry(root, width=50, bg="gray", fg="white")

def selecionar_pasta():
    pasta_entry.delete(0, tk.END)
    pasta_selecionada = filedialog.askdirectory()
    pasta_entry.insert(0, pasta_selecionada)
    pasta_label.config(text=f"Pasta selecionada: {pasta_selecionada}")

selecionar_button = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta, font=("Roboto", 13), bg="#1D8C83", fg="#FFFFFF", border="5")

# Pasta de saída
output_label = tk.Label(root, text="Pasta de saída não selecionada.", font=("Roboto", 10), bg="#333333", fg="white")
output_entry = tk.Entry(root, width=50, bg="gray", fg="white")

def selecionar_output():
    output_entry.delete(0, tk.END)
    output_selecionada = filedialog.askdirectory()
    output_entry.insert(0, output_selecionada)
    output_label.config(text=f"Pasta de saída: {output_selecionada}")

selecionar_output_button = tk.Button(root, text="Selecionar Pasta de Saída", command=selecionar_output, font=("Roboto", 13), bg="#1D8C83", fg="#FFFFFF", border="5")

# Arquivo Excel
excel_label = tk.Label(root, text="Arquivo Excel não selecionado.", font=("Roboto", 10), bg="#333333", fg="white")
excel_entry = tk.Entry(root, width=50, bg="gray", fg="white")

def selecionar_excel():
    excel_entry.delete(0, tk.END)
    excel_selecionado = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    excel_entry.insert(0, excel_selecionado)
    excel_label.config(text=f"Arquivo Excel: {excel_selecionado}")

selecionar_excel_button = tk.Button(root, text="Selecionar Arquivo Excel", command=selecionar_excel, font=("Roboto", 13), bg="#1D8C83", fg="#FFFFFF", border="5")

iniciar_button = tk.Button(root, text="Iniciar Extração", command=iniciar_extracao, font=("Roboto", 13), bg="#1D8C83", fg="#FFFFFF", border="5")

resultado_label = tk.Label(root, text="", font=("Roboto", 12), bg="#333333", fg="white")
direitos_autorais = tk.Label(root, text="© 2023 Axxen. Todos os direitos reservados.", font=("Arial", 10), bg="#333333", fg="white")

img = PhotoImage(file = "axxenoficial.png")
label_imagem = Label(root, image=img, bg="#333333").pack()

root.geometry("800x800")

tk.Label(root, text=" ", bg="#333333").pack()
nome_programa2.pack()
tk.Label(root, text=" ", bg="#333333").pack()
instrucoes_label.pack()
tk.Label(root, text=" ", bg="#333333").pack()

# Widgets da pasta de entrada
pasta_label.pack()
pasta_entry.pack()
selecionar_button.pack()
tk.Label(root, text=" ", bg="#333333").pack()

# Widgets da pasta de saída
output_label.pack()
output_entry.pack()
selecionar_output_button.pack()
tk.Label(root, text=" ", bg="#333333").pack()

# Widgets do arquivo Excel
excel_label.pack()
excel_entry.pack()
selecionar_excel_button.pack()
tk.Label(root, text="", bg="#333333").pack()

iniciar_button.pack()
tk.Label(root, text="", bg="#333333").pack()
resultado_label.pack()
direitos_autorais.pack(side="bottom")

root.mainloop()
