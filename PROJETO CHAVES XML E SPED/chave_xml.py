import os
import xml.etree.ElementTree as ET
import threading

def extrair_chave_nota(xml_file, todas_chaves_notas):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        chave_nota_infNFe = root.find('.//{http://www.portalfiscal.inf.br/nfe}infNFe')
        if chave_nota_infNFe is not None:
            chave_nota = chave_nota_infNFe.get('Id').strip()
            todas_chaves_notas.append(chave_nota[3:])

        chave_nota_infEvento = root.find('.//{http://www.portalfiscal.inf.br/nfe}infEvento')
        if chave_nota_infEvento is not None:
            chave_nota = chave_nota_infEvento.get('Id').strip()
            todas_chaves_notas.append(chave_nota[2:])
    except Exception as e:
        print(f"Erro ao extrair chave do arquivo {xml_file}: {e}")

def extrair_chaves_notas_pasta(pasta_entrada):
    todas_chaves_notas = []

    # Lista os arquivos XML na pasta de entrada
    arquivos_xml = [os.path.join(pasta_entrada, arquivo) for arquivo in os.listdir(pasta_entrada) if arquivo.endswith(".xml")]

    # Lista para armazenar as threads
    threads = []

    # Processa cada arquivo XML em uma thread separada
    for arquivo_xml in arquivos_xml:
        thread = threading.Thread(target=extrair_chave_nota, args=(arquivo_xml, todas_chaves_notas))
        thread.start()
        threads.append(thread)

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    return todas_chaves_notas

# Pasta de entrada contendo os arquivos XML
pasta_entrada_xml = "Z:\\ANE\\ICMS ST\\PROJETO ALTESE\\XML´S\\XMLS"

# Extrai as chaves das notas fiscais de todos os arquivos na pasta XML
chaves_notas = extrair_chaves_notas_pasta(pasta_entrada_xml)

# Caminho do arquivo de saída para todas as chaves
arquivo_saida = 'chaves_notas.txt'

# Escreve as chaves em um arquivo de texto
with open(arquivo_saida, 'w', encoding='utf-8') as f:
    for chave in chaves_notas:
        f.write(chave + '\n')

print(f"As chaves das notas fiscais foram extraídas e salvas em '{arquivo_saida}'.")
