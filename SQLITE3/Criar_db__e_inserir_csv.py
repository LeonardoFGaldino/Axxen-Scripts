import sqlite3
import csv

def create_database(db_file, table_name, columns):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()



    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(['col_{} TEXT'.format(idx) for idx, col in enumerate(columns)])});"

    cursor.execute(create_table_query)


    conn.commit()
    conn.close()

def csv_to_sqlite(csv_file, db_file, table_name):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()


    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = [
            'id',
            'cnpj',
            'simples',
            'simples_data_inicio',
            'simples_data_fim'
                'mei',
            'mei_inicio',
            'mei_fim'
        ]


        create_database(db_file, table_name, header)


        insert_query = f"INSERT INTO {table_name} VALUES (NULL, {', '.join(['?' for _ in header])});"

        for row in csv_reader:
            row = row[0].split(';')
            cursor.execute(insert_query, row)


    conn.commit()
    conn.close()

# Substitua 'caminho/do/seu/banco.db', 'sua_tabela' e 'caminho/do/seu/arquivo.csv' pelos caminhos corretos do seu banco de dados, nome desejado para a tabela e caminho do seu arquivo CSV, respectivamente.
db_file_path = 'db_file.db'
table_name = 'empresa'
csv_file_path = 'F.K03200$W.SIMPLES.CSV.D40113'

csv_to_sqlite(csv_file_path, db_file_path, table_name)
