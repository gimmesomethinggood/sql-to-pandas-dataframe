import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('''
          SELECT
          *
          FROM products
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_id', 'product_name', 'price'])
#print(df)

'''
# get max price
max_price = df['price'].max()
print (max_price)
'''

#list column names
print(df.columns.values)

#rename $ with blank in every column name
df.columns = df.columns.str.replace('_', '_$_')

#list column names
print(df.columns.values)

# writing data frame to a CSV file
df.to_csv('products_renamed.csv')