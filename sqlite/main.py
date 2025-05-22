import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    author VARCHAR(100),
    price FLOAT
);
''')

cursor.execute('''
INSERT INTO books (title, author, price) VALUES ('Hamlet', 'William Shakespeare', 10.5);

''')
cursor.execute('SELECT * FROM books')

conn.close()