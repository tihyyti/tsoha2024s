from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class PieceOfNewsHeader(db.Model):
    __tablename__ = 'PieceOfNewsHeader'

    id = db.Column(db.Integer, primary_key=True)
    started_by = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    header = db.Column(db.String, nullable=False)
    number_of_piece_of_news_content = db.Column(db.Integer, nullable=False)
    started = db.Column(db.DateTime, default=datetime.utcnow)

    piece_of_news_headers = db.relationship('PieceOfNewsHeader', backref='genre', lazy=True)
    piece_of_news_contents = db.relationship('PieceOfNewsContent', backref='news_header', lazy=True)

    def __init__(self, started_by, genre, header, number_of_piece_of_news_content, started = None):
        self.started_by = started_by
        self.genre = genre
        self.header = header
        self.number_of_piece_of_news_content = number_of_piece_of_news_content
        self.started = started or datetime.utcnow()

    def get_piece_of_news_contents(self):
        if self.piece_of_news_contents is None:
            self.piece_of_news_contents = []
        return self.piece_of_news_contents

    def add_piece_of_news_content(self, piece_of_news_content):
        if self.piece_of_news_contents is None:
            self.piece_of_news_contents = []
        self.piece_of_news_contents.append(piece_of_news_content)
        return self.piece_of_news_contents

    def del_piece_of_news_content(self, piece_of_news_content):
        if self.piece_of_news_contents is None:
            return
        self.piece_of_news_contents.remove(piece_of_news_content)


    def __init__(self, started_by=None, genre=None, header=None, number_of_piece_of_news_content=0, started=None):
        self.started_by = started_by
        self.genre = genre
        self.header = header
        self.number_of_piece_of_news_content = number_of_piece_of_news_content
        self.started = started or datetime.utcnow()

    def get_initiator(self):
        return self.started_by

    def set_initiator(self, started_by):
        self.started_by = started_by

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_started(self):
        return self.started

    def set_started(self, started):
        self.started = started

    def get_number_of_piece_of_news_content(self):
        return self.number_of_piece_of_news_content

    def set_number_of_piece_of_news_content(self, number_of_piece_of_news_content):
        self.number_of_piece_of_news_content = number_of_piece_of_news_content

