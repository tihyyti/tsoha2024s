from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class NewsHeaderList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.Integer)
    header = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    latest = db.Column(db.String(255))

    def __init__(self, genre, header, amount, latest):
        self.genre = genre
        self.header = header
        self.amount = amount
        self.latest = latest

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)