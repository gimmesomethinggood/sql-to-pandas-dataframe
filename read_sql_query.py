import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database')

sql_query = pd.read_sql_query('''
                               SELECT
                               *
                               FROM products
                               ''', conn)

df = pd.DataFrame(sql_query, columns=['product_id', 'product_name', 'price'])
print(df)


