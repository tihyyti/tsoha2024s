"""
I’ll add the relevant methods from your Spring Boot snippet to the previous User class in Python Flask. This will include constructors and a method to get the username.

In this updated User class:
The __init__ method acts as a constructor, initializing userName,
password, and the lists for newsGenres, pieceOfNewsHeaders, and
pieceOfNewsContents.
The get_user_name method returns the userName.
This setup mirrors the constructors and methods from your Spring Boot
@Entity code.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=True)

    newsGenres = relationship('NewsGenre', backref='editor', lazy='dynamic')
    pieceOfNewsHeaders = relationship('PieceOfNewsHeader', backref='startedBy', lazy='dynamic')
    pieceOfNewsContents = relationship('PieceOfNewsContent', backref='editorID', lazy='dynamic')

    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password if password else ""
        self.newsGenres = []
        self.pieceOfNewsHeaders = []
        self.pieceOfNewsContents = []

    def get_user_name(self):
        return self.userName

    def get_news_genres(self):
        if self.newsGenres is None:
            self.newsGenres = []
        return self.newsGenres

class NewsGenre(db.Model):
    __tablename__ = 'newsgenre'
    id = db.Column(db.Integer, primary_key=True)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    genre_name = db.Column(db.String(100), nullable=False)

class PieceOfNewsHeader(db.Model):
    __tablename__ = 'pieceofnewsheader'
    id = db.Column(db.Integer, primary_key=True)
    started_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    header = db.Column(db.String(100), nullable=False)

class PieceOfNewsContent(db.Model):
    __tablename__ = 'pieceofnewscontent'
    id = db.Column(db.Integer, primary_key=True)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
