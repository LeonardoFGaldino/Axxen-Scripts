import sqlite3
import pandas as pd

def export_sqlite_to_excel_partially(db_file2, table_name2, excel_file, chunk_size=1000):

    conn = sqlite3.connect(db_file2)


    count_query = f"SELECT COUNT(*) FROM {table_name2};"
    total_records = conn.execute(count_query).fetchone()[0]


    num_parts = -(-total_records // chunk_size)

    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

    for part in range(num_parts):

        offset = part * chunk_size
        limit = chunk_size


        query = f"SELECT * FROM {table_name2} LIMIT {limit} OFFSET {offset};"


        df = pd.read_sql_query(query, conn)


        sheet_name = f'Part_{part + 1}'
        df.to_excel(writer, sheet_name=sheet_name, index=False)


    conn.close()


    writer.save()


db_file_path = 'db_file2.db'
table_name = 'table_name2'
excel_file_path = 'arquivo_excel2.xlsx'

export_sqlite_to_excel_partially(db_file_path, table_name, excel_file_path, chunk_size=1000)
