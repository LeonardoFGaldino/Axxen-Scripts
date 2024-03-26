from datetime import datetime, timedelta
import pandas as pd
import sqlite3
import logging
from tkinter import filedialog
import tkinter as tk

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CNPJInfoLogic:
    @staticmethod
    def process_data(df_excel):
        conn_simples = sqlite3.connect("simples_nacional.sqlite3")
        cursor_simples = conn_simples.cursor()
        today = datetime.now()
        ultima_atualizacao = datetime.now() - timedelta(days=3 * 30)
        results = []

        for idx, row in df_excel.iterrows():
            cnpj_excel = row['CNPJ Participante']
            data_doc = row['Data Documento']
            if pd.isna(data_doc) or not cnpj_excel:
                results.append('Analisar')
                continue

            data_doc = datetime.strptime(str(data_doc), "%d/%m/%Y")
            target = 'Não'

            cnpj_excel = str(cnpj_excel)
            cnpj_excel = cnpj_excel[:8]

            cursor_simples.execute(f"SELECT simples.opcao_simples, simples.simples_inicio, simples.simples_fim FROM simples WHERE cnpj = '{cnpj_excel}';")
            data = cursor_simples.fetchone()

            if data:
                simples, entrada, exclusao = data
                entrada = datetime.strptime(entrada, '%Y%m%d')

                if exclusao == '00000000' and simples == 'S':
                    exclusao = today
                else:
                    exclusao = datetime.strptime(exclusao, '%Y%m%d')

                if data_doc > ultima_atualizacao:
                    target = 'Analisar'
                elif data_doc <= exclusao:
                    target = 'Sim' if data_doc > entrada else 'Analisar'

            results.append(target)

        conn_simples.close()
        df_excel['Opção Simples'] = results

        try:
            conn_cnpj = sqlite3.connect("db_file2.db")
            cursor_cnpj = conn_cnpj.cursor()

            result_list = []

            for idx, row in df_excel.iterrows():
                cnpj_excel = str(row['CNPJ Participante'])
                if pd.notna(cnpj_excel):
                    cnpj_excel = cnpj_excel.split('.')[0]

                classificacao = CNPJInfoLogic.get_classificacao(cursor_cnpj, cnpj_excel)

                result_list.append({'CNPJ': cnpj_excel, 'Classificação': classificacao})

        finally:
            conn_cnpj.close()

        result_df = pd.DataFrame(result_list)
        df_excel['Cnpj'] = result_df['CNPJ']
        df_excel['Classificação'] = result_df['Classificação']

        return df_excel

    @staticmethod
    def get_classificacao(cursor, cnpj):
        cursor.execute(f"SELECT classe FROM cnpj WHERE codigo = '{cnpj}';")
        result = cursor.fetchone()
        return result[0] if result else ''

def process_excel():
    logger = logging.getLogger()
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    logger.warning(file_path)
    if file_path:
        logger.warning('Abrindo arquivo')
        df_excel = pd.read_excel(file_path, dtype=str)
        logger.warning('Processando dados')
        result_df = CNPJInfoLogic.process_data(df_excel)

        export_path = filedialog.askdirectory()
        if export_path:
            save_path = f"{export_path}/testey.xlsx"
            result_df.to_excel(save_path, index=False)
            logger.warning(f"Resultados exportados para {save_path}")
        else:
            logger.warning("Nenhum diretório de exportação selecionado.")
    else:
        logger.warning("Caminho do arquivo inválido.")

if __name__ == "__main__":
    process_excel()
