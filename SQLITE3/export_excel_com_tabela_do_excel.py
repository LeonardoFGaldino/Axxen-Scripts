import sqlite3
import pandas as pd

def export_sqlite_to_excel(db_file, table_name, excel_file):

    conn = sqlite3.connect(db_file)


    query = f"SELECT * FROM {table_name};"


    df = pd.read_sql_query(query, conn)


    df['CNPJ_BASICO'] = ""
    df['OPCAO_PELO_SIMPLES'] = ""
    df['DATA_OPCAO_SIMPLES'] = ""
    df['DATA_EXCLUSAO_SIMPLES'] = ""
    df['OPCAO_PELO_MEI'] = ""
    df['DATA_OPCAO_MEI'] = ""
    df['DATA_EXCLUSAO_MEI'] = ""


    df = df[['CNPJ_BASICO', 'OPCAO_PELO_SIMPLES', 'DATA_OPCAO_SIMPLES', 'DATA_EXCLUSAO_SIMPLES', 'OPCAO_PELO_MEI', 'DATA_OPCAO_MEI', 'DATA_EXCLUSAO_MEI'] + list(df.columns[:-7])]


    df.to_excel(excel_file, index=False)


    conn.close()


db_file_path = 'db_file.db_part100.db'
table_name = 'table_name'
excel_file_path = 'arquivo_excel.xlsx'

export_sqlite_to_excel(db_file_path, table_name, excel_file_path)
