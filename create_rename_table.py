import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products_rename
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [amount] INTEGER)
          ''')

conn.commit()