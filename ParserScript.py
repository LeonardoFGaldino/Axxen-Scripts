import os
from glob import glob

import nfe
import nfe_evento
import nfe_proc
import cte
import cte_evento
import resEvento
import resNFe


def parse_nao_processado(folder):
    unprocessed_files = []

    for arquivo_xml in glob(os.path.join(folder, '**/*.xml'), recursive=True):
        if arquivo_xml.endswith('.xml'):
            caminho_completo = os.path.join(folder, arquivo_xml)

            try:
                parsed = nfe.parse(caminho_completo) or \
                         nfe_evento.parse(caminho_completo) or \
                         nfe_proc.parse(caminho_completo) or \
                         cte.parse(caminho_completo) or \
                         cte_evento.parse(caminho_completo) or \
                         resEvento.parse(caminho_completo) or \
                         resNFe.parse(caminho_completo)

                if parsed is None:
                    unprocessed_files.append(caminho_completo)

            except Exception as e:
                print(f"Error processing {caminho_completo}: {str(e)}")
                unprocessed_files.append(caminho_completo)

    return unprocessed_files


pasta_xml = "C:/Users/Admin/Desktop/xmls_leve"


arquivos_nao_processados = parse_nao_processado(pasta_xml)


l4 = []

for arquivo in arquivos_nao_processados:
    if arquivo in nfe.__dict__ and arquivo in cte.__dict__ and \
       arquivo in nfe_evento.__dict__ and arquivo in resNFe.__dict__ and \
       arquivo in resEvento.__dict__ and arquivo in nfe_proc.__dict__ and \
       arquivo in cte_evento.__dict__:
        l4.append(arquivo)

print("Arquivos não processados:", l4)
