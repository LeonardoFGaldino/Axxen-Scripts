import sqlite3

def drop_table(db_file, table_name):
    try:

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()


        drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(drop_table_query)


        conn.commit()
        print(f'Tabela {table_name} excluída com sucesso.')
    except sqlite3.Error as e:
        print(f"Erro ao excluir a tabela: {e}")
    finally:
        conn.close()


db_file_path = 'db_file.db'
table_name_to_drop = 'table_name'

drop_table(db_file_path, table_name_to_drop)
