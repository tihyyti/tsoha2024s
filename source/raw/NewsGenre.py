from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class NewsGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.Integer)
    editor = db.Column(db.Integer)
    header = db.Column(db.String(255))

    def __init__(self, genre, editor, header):
        self.genre = genre
        self.editor = editor
        self.header = header

    def set_piece_of_news_headers(self, piece_of_news_headers):
        self.piece_of_news_headers = piece_of_news_headers

    def get_piece_of_news_headers(self):
        if not self.piece_of_news_headers:
            self.piece_of_news_headers = []
        return self.piece_of_news_headers

    def add_piece_of_news_header(self, piece_of_news_header):
        if not self.piece_of_news_headers:
            self.piece_of_news_headers = []
        self.piece_of_news_headers.append(piece_of_news_header)
        return self.piece_of_news_headers

    def del_piece_of_news_header(self, piece_of_news_header):
        if not self.piece_of_news_headers:
            return
        self.piece_of_news_headers.remove(piece_of_news_header)

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_editor(self):
        return self.editor

    def set_editor(self, editor):
        self.editor = editor

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)