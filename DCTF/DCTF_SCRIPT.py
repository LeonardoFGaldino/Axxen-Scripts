# # Abrindo o arquivo original novamente para realizar as alterações nas linhas exatas informadas
# file_path = "C:\\Users\\Axxen\\Desktop\\teste dctf\\74017930000194-DCTFM37-202111-RETIF.dec.txt"
#
# # Lendo o conteúdo do arquivo
# with open(file_path, 'r') as file:
#     content = file.readlines()
#
# # Valores fornecidos pelo usuário
# pis_antigo = "2423191"
# pis_novo = "2233444"
# cofins_antigo = "11661715"
# cofins_novo = "11557777"
#
# # Lista para armazenar o conteúdo modificado
# new_content = []
#
# # Percorrendo cada linha e fazendo as alterações necessárias
# for line in content:
#     # Substituição do valor PIS/PASEP
#     if pis_antigo in line:
#         line = line.replace(pis_antigo, pis_novo)
#     # Substituição do valor COFINS
#     if cofins_antigo in line:
#         line = line.replace(cofins_antigo, cofins_novo)
#
#     # Adiciona a linha modificada na nova lista de conteúdo
#     new_content.append(line)
#
# # Salvando o arquivo com as modificações exatas
# output_path = 'C:\\Users\\Axxen\\Desktop\\teste dctf\\RETIF_FINAL.txt'
# with open(output_path, 'w') as file:
#     file.writelines(new_content)
#
# output_path


'''SUPONDO OS VALORES ANTIGOS PARA A SUBSTITUIÇÃO'''


# Abrindo o arquivo original novamente para realizar as alterações nas linhas exatas informadas
file_path = "C:\\Users\\Axxen\\Desktop\\teste dctf\\74017930000194-DCTFM37-202111-RETIF.dec.txt"

# Lendo o conteúdo do arquivo
with open(file_path, 'r') as file:
    content = file.readlines()

# Solicitando os valores ao usuário
pis_antigo = input("Digite o valor antigo do PIS/PASEP: ")
pis_novo = input("Digite o novo valor do PIS/PASEP: ")
cofins_antigo = input("Digite o valor antigo do COFINS: ")
cofins_novo = input("Digite o novo valor do COFINS: ")

# Lista para armazenar o conteúdo modificado
new_content = []

# Percorrendo cada linha e fazendo as alterações necessárias
for line in content:
    # Substituição do valor PIS/PASEP
    if pis_antigo in line:
        line = line.replace(pis_antigo, pis_novo)
    # Substituição do valor COFINS
    if cofins_antigo in line:
        line = line.replace(cofins_antigo, cofins_novo)

    # Adiciona a linha modificada na nova lista de conteúdo
    new_content.append(line)

# Salvando o arquivo com as modificações exatas
output_path = 'C:\\Users\\Axxen\\Desktop\\teste dctf\\RETIF_FINAL3.txt.dec'
with open(output_path, 'w') as file:
    file.writelines(new_content)

print(f"Arquivo salvo em: {output_path}")






