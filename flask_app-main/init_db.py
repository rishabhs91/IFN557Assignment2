import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Samsung S23 Ultra 5G 1TB (Green)', 'Samsung S23 Smartphone', 'S23', 2649)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Apple iPhone 15 Pro Max 512GB (Natural Titanium)', 'IPhone 15 Smartphone', 'Iphone15', 2549)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Motorola Edge 30 Ultra 5G 256GB (Interstellar Black)', 'Motorola Smartphone', 'Motorola', 1399)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Asus Zenfone 10 5G 512GB (Midnight Black)', 'ASUS Smartphone', 'Asus', 1499)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('Google Pixel 7a 5G 128GB (Charcoal)', 'Google Pixel 7a Smartphone', 'GooglePixel', 749)
            )

cur.execute("INSERT INTO products (name, description, image, price) VALUES (?, ?, ?, ?)",
            ('OPPO Reno10 5G 256GB (Ice Blue)', 'Oppo Smartphone', 'Oppo', 749)
            )

connection.commit()
connection.close()