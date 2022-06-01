from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/xddddd.db'.format(os.getcwd())
# print(dir(db.Model))
# print(help(db.Model))
db = SQLAlchemy(app)

db.create_all() >>>tworzy bazę
form plik import db
from gdzies import Item

class Item(db.Model):
    id = db.Column(db.Integer(), primaty_key = True)
    id = db.Column(db.String(length=10), nullable=False)
    id = db.Column(db.Integer(), nullable=False, unique=True)
    id = db.Column(db.String(length=10))

item1 = Item(name='nazwa', etc)

db.session.add(item1)
db.session.commit()
Item.query.all() >>> zwraca listę po której można iterować w teminalnu

for item in Item.query.filter_by(price=500):
    item_name