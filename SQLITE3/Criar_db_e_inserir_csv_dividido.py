import sqlite3
import csv
import os

def create_database(db_file, table_name, columns):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()


    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(['col_{} TEXT'.format(idx) for idx, col in enumerate(columns)])});"
    cursor.execute(create_table_query)


    conn.commit()
    conn.close()

def csv_to_sqlite(csv_file, db_file_prefix, table_name, chunk_size=50000):

    if not os.path.isfile(csv_file):
        print(f'O arquivo CSV {csv_file} não existe.')
        return

    part_number = 1


    conn = sqlite3.connect(f"{db_file_prefix}_part{part_number}.db")
    cursor = conn.cursor()


    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)


        create_database(f"{db_file_prefix}_part{part_number}.db", table_name, header)


        insert_query = f"INSERT INTO {table_name} VALUES (NULL, {', '.join(['?' for _ in header])});"
        count = 0
        for row in csv_reader:
            cursor.execute(insert_query, row)
            count += 1
            if count == chunk_size:
                conn.commit()
                conn.close()


                part_number += 1
                conn = sqlite3.connect(f"{db_file_prefix}_part{part_number}.db")
                cursor = conn.cursor()


                create_database(f"{db_file_prefix}_part{part_number}.db", table_name, header)

                count = 0


    conn.commit()
    conn.close()


csv_file_path = 'F.K03200$W.SIMPLES.CSV.D40113'
db_file_prefix = 'db_file.db'
table_name = 'table_name'

csv_to_sqlite(csv_file_path, db_file_prefix, table_name)
