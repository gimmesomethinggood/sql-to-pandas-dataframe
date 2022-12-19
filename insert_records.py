import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('''
          INSERT INTO products (product_id, product_name)

                VALUES
                (1,'Computer'),
                (2,'Printer'),
                (3,'Tablet'),
                (4,'Desk'),
                (5,'Chair')
          ''')

c.execute('''
          INSERT INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          ''')

conn.commit()