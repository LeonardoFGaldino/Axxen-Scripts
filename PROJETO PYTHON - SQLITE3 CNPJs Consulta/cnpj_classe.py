import sqlite3
import pandas as pd

class CNPJInfoLogic:
    def __init__(self, cache):
        self.cache = cache

    def process_data(self, df_excel):
        try:
            conn = sqlite3.connect("db_file2.db")
            cursor = conn.cursor()

            result_list = []  # Use a list to store rows

            for idx, row in df_excel.iterrows():
                cnpj_excel = str(row['CNPJ Participante'])  # Convert to string
                if pd.notna(cnpj_excel):
                    cnpj_excel = cnpj_excel.split('.')[0]  # Remove decimal part if present

                # Print the CNPJ for debugging
                print(f"Processing CNPJ: {cnpj_excel}")

                classificacao = self.get_classificacao(conn, cnpj_excel)  # Use self.get_classificacao

                # Print the result for debugging
                print(f"Classificação: {classificacao}")

                result_list.append({'CNPJ': cnpj_excel, 'Classificação': classificacao})

        finally:
            conn.close()

        # Print the list for debugging
        print(result_list)

        # Convert the list to a DataFrame
        result_df = pd.DataFrame(result_list)
        result_df.to_excel('base_cnpj_classe.xlsx', index=False)

    def get_classificacao(self, conn, cnpj: str) -> str:
        query = f'''
            SELECT classe
            FROM cnpj
            WHERE codigo = \'{cnpj}\'
        '''
        print(f"Executing query: {query}")  # Print the query for debugging
        cur = conn.execute(query)
        result = cur.fetchone()

        # Print the result for debugging
        print(f"Query result: {result}")

        return result[0] if result else ''


# Note: You might need to adjust the SQL query based on your actual schema and logic.

cache_conn = sqlite3.connect(":memory:")
cache = cache_conn.cursor()

excel_df = pd.read_excel("C:\\Users\\Admin\\Desktop\\CNPJ Planilha.xlsx")

# Create an instance of CNPJInfoLogic and call the process_data method
CNPJInfoLogic(cache).process_data(excel_df)

cache_conn.close()
