import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable, false

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'book_db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Books(db.module):
    id = db.Column(db.Integer, primar_key = True)
    title = db.Column(db.String(35), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f"title: {self.title}\n, author: {self.author}, price: {self.price}"


with app.app_context():
    book1 = Books.query.first()
    print(book1)