import sqlite3
import pandas as pd


conn = sqlite3.connect('test_database')
c = conn.cursor()

#sql_query = pd.read_sql_query('''
#                               SELECT
#                               *
#                               FROM products
#                               ''', conn)

#df = pd.DataFrame(sql_query, columns=['product_id', 'product_name', 'price'])
#print(df)


#df.to_sql('products_copy', conn, if_exists='replace', index = False)
#print(df)

c.execute('''
          SELECT
          *
          FROM products_copy
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_id', 'product_name', 'price'])
print(df)