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

# columns
dfc = df.columns
print(dfc)

# rename in place (Change a single column header name)
df.rename(columns={'price' : 'amount'}, inplace=True)
print(df)

# copy newly renamed data frame/data to new table.
df.to_sql('products_rename', conn, if_exists='append', index = False)

# to csv
df.to_csv('products_renamed.csv', index=False)

