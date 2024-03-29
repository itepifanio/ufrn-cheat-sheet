# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_sqlite.ipynb.

# %% auto 0
__all__ = ['ReadOnlyInMemorySQLite']

# %% ../nbs/01_sqlite.ipynb 3
import sqlite3
import pandas as pd

# %% ../nbs/01_sqlite.ipynb 6
class ReadOnlyInMemorySQLite:
    def __init__(self):
        self.connection = sqlite3.connect('file:storage.db?mode=memory&cache=shared', uri=True, check_same_thread=False)
        try:
            self.load_csv_as_table('turma_matricula_docente_filtrados.csv', 'data')
        except FileNotFoundError:
            print("CSV file not found. Skipping table loading.")

    def load_csv_as_table(self, csv_path, table_name):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, self.connection, if_exists='replace', index=False)

    def execute_query(self, query):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
