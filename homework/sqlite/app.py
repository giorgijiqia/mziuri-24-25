import sqlite3

conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

queries = {
    " ყველა წიგნი შექსპირის":
        "SELECT * FROM books WHERE author = 'William Shakespeare';",

    " წიგნები, რომელიც დაწერილია შექსპირის ან Rowling-ის მიერ":
        "SELECT * FROM books WHERE author = 'William Shakespeare' OR author = 'Rowling';",

    " წიგნები რომლის ფასი არ აღემატება 20 ლარს":
        "SELECT * FROM books WHERE price <= 20;",

    " წიგნის ავტორები (განმეორებების გარეშე)":
        "SELECT DISTINCT author FROM books;",

    " იმ მომხმარებელთა სახელები, რომლებსაც ბალანსზე აქვთ 100 ლარზე მეტი თანხა":
        "SELECT username FROM users WHERE balance > 100;",

    " წიგნების შესახებ მონაცემები, რომლებიც გაიყიდა 2018 წლამდე":
        """
        SELECT DISTINCT books.*
        FROM books
        INNER JOIN purchase ON books.id = purchase.book_id            
        WHERE purchase.purchase_date < '2018-01-01';
        """,

    " იმ მომხმარებლების მონაცემები, რომლებმაც 2018 წელს იყიდეს წიგნი":
        """
        SELECT DISTINCT users.*
        FROM users
        INNER JOIN purchase ON users.id = purchase.user_id
        WHERE strftime('%Y', purchase.purchase_date) = '2018';
        """,

    " იმ მომხმარებლების მონაცემები, რომლებსაც აქვთ ერთი წიგნი მაინც შესყიდული":
        """
        SELECT DISTINCT users.*
        FROM users
        INNER JOIN purchase ON users.id = purchase.user_id;
        """,

    " იმ წიგნების დასახელება, რომლებიც ერთხელ მაინც გაიყიდა":
        """
        SELECT DISTINCT books.title
        FROM books
        INNER JOIN purchase ON books.id = purchase.book_id;
        """
}

for description, query in queries.items():
    print(f"\n--- {description} ---")
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

conn.close()

"inner joinit ორ ცხრილს ვაკავშირებთ ერთმანეთთან როცა ორივეში არსებობს ერთნაირი მონაცემები"