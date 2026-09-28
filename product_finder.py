import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        category TEXT NOT NULL,
        price DOUBLE NOT NULL,
        rating DOUBLE,
        in_stock INTEGER DEFAULT 1 
    )
""")


products = [
    ("Wireless Mouse", "Accessories", 29.99, 4.5, 1),
    ("Mechanical Keyboard", "Accessories", 89.99, 4.8, 1),
    ("USB-C Hub", "Accessories", 34.99, 4.2, 0),
    ("27-inch Monitor", "Displays", 299.99, 4.6, 1),
    ("24-inch Monitor", "Displays", 179.99, 4.3, 1),
    ("Webcam HD", "Accessories", 49.99, 3.9, 1),
    ("Noise-Canceling Headphones", "Audio", 199.99, 4.7, 1),
    ("Bluetooth Speaker", "Audio", 59.99, 4.1, 0),
    ("Laptop Stand", "Accessories", 39.99, 4.4, 1),
    ("External SSD 1TB", "Storage", 89.99, 4.6, 1),
    ("External SSD 2TB", "Storage", 149.99, 4.5, 1),
    ("Flash Drive 64GB", "Storage", 12.99, 4.0, 1),
]

cursor.executemany("""
    INSERT INTO products (name, category, price, rating, in_stock) VALUES (?, ?, ?, ?, ?)
""", products)

connection.commit()

cursor.execute("""
    SELECT name, category
    FROM products
    WHERE in_stock = 0
""")

print("===Out of Stock Products===")
for row in cursor.fetchall():
    print(f"  {row[0]} | {row[1]} ")

cursor.execute("""
    SELECT name, rating , price 
    FROM products
    WHERE rating >= 4.5 AND price < 100.00
""")

print("===Products by Ratings and Price===")
for row in cursor.fetchall():
     print(f"  {row[0]} | {row[1]} ${row[2]}")

cursor.execute("""
    SELECT name, price  
    FROM products
    WHERE category = 'Accessories'
    ORDER BY price DESC
    LIMIT 3
""")

print("===3 Most Expensive Products===")
for row in cursor.fetchall():
    print(f"  {row[0]} | {row[1]} ")


cursor.execute("""
    SELECT name, category, price, rating, in_stock
    FROM products
    WHERE name 
""")

print("===Products with Monitor in the Name===")
for row in cursor.fetchall():
    print(f"  {row[0]} | {row[1]} | ${row[2]} | {row[3]} | {row[4]} ")

cursor.execute("""
    SELECT name, category, price
    FROM products
    WHERE category != 'Accessories' AND in_stock > 0
    ORDER BY category, price 
""")

print("===Products in STOCK but NOT Accessories===")
for row in cursor.fetchall():
    print(f"  {row[0]} | {row[1]} | ${row[2]}")