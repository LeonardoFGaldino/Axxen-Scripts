import sqlite3

conn = sqlite3.connect('db_file.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT NOT NULL,
        simples INTEGER NOT NULL,
        entrada_simples INTEGER NOT NULL,
        exclusao_simples INTEGER NOT NULL,
        mei INTEGER NOT NULL,
        entrada_mei INTEGER NOT NULL,
        exclusao_mei INTEGER NOT NULL
    )
''')


conn.close()