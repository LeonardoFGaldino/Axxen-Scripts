import sqlite3
import pandas as pd

def export_sqlite_to_excel(db_file, table_name, excel_file):

    conn = sqlite3.connect(db_file)


    query = f"SELECT * FROM {table_name};"


    df = pd.read_sql_query(query, conn)


    df.to_excel(excel_file, index=False)


    conn.close()


db_file_path = 'db_file.db'
table_name = 'table_name'
excel_file_path = 'arquivo_excel.xlsx'

export_sqlite_to_excel(db_file_path, table_name, excel_file_path)
