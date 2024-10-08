from datetime import datetime
import pandas as pd
import sqlite3
import logging
import timedelta
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CNPJInfoLogic:
    @staticmethod
    def process_data(df_excel):
        conn = sqlite3.connect("C:\\Users\\Admin\\Downloads\\Simples\\simples_nacional.sqlite3")
        cursor = conn.cursor()
        today = datetime.now()
        ultima_atualizacao = datetime.now() - timedelta.Timedelta(days=3 * 30)
        results = []
        df_excel.fillna('') #PREENCHE VALORES NULOS NO DATAFRAME

        for idx, row in df_excel.iterrows(): #ITERA SOBRE AS LINHAS DO DATAFRAME
            cnpj_excel = row['CNPJ Participante'] #OBTEM O VALOR DA COLUNA 'CNPJ Participante' pra linha atual
            if cnpj_excel == '24537452000175':
                print('ok')
            data_doc = row['Data Documento'] # OBTEM O VALOR DA COLUNA 'Data Documento' para linha atual
            if (not data_doc or data_doc is np.nan) or not cnpj_excel:
                results.append('Analisar')
                continue

            data_doc = datetime.strptime(str(data_doc), "%d/%m/%Y") #CONVERTE A DATA
            target = 'Não'

            logger.warning(f"Processando CNPJ: {cnpj_excel}")
            cnpj_excel = str(cnpj_excel)
            cnpj_excel = cnpj_excel[:8]

            cursor.execute(f"SELECT simples.opcao_simples, simples.simples_inicio, simples.simples_fim FROM simples WHERE cnpj = '{cnpj_excel}';")
            data = cursor.fetchone()

            logger.warning(f"Reultado da consulta para CNPJ {cnpj_excel}: {data}")
            if data:
                simples, entrada, exclusao = data
                entrada = datetime.strptime(entrada, '%Y%m%d') #CONVERTE A DATA

                if exclusao == '00000000' and simples == 'S':
                    exclusao = today
                else:
                    exclusao = datetime.strptime(exclusao, '%Y%m%d')

                # Se data da nota estiver nos ultimos 3 meses cnpj deve ser analisado
                if data_doc > ultima_atualizacao:
                    target = 'Analisar'
                # Se data da nota estiver dentro do período em que cnpj foi simples target é igual a S
                elif data_doc <= exclusao:
                    # Se data do documento for menor que data de entrada do ultimo periodo do simples, o cnpj deve ser analisado.
                    # Caso contrario o cnpj era do simples no periodo em questão.
                    target = 'Sim' if data_doc > entrada else 'Analisar'

            results.append(target)

        conn.close()
        df_excel['Opção Simples'] = results
        return df_excel
