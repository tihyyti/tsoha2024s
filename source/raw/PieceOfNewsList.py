from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PieceOfNewsList(db.Model):
    __tablename__ = 'PieceOfNewsList'

    id = db.Column(db.Integer, primary_key=True)
    editor_id = db.Column(db.Integer, nullable=False)
    piece_of_news_header = db.Column(db.Integer, nullable=False)
    editor = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    send_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, editor_id = -1, piece_of_news_header = -1, editor = "Toimittaja", content = "Uutinen", send_time = None):
        self.editor_id = editor_id
        self.piece_of_news_header = piece_of_news_header
        self.editor = editor
        self.content = content
        self.send_time = send_time or datetime.utcnow()

    def __init__(self, rowi, editor, content):
        self.editor_id = 1
        self.piece_of_news_header = 1
        self.editor = editor
        self.content = content
        self.send_time = datetime.utcnow()

    def __init__(self, rowi, editor_id, piece_of_news_header, editor, content, send_time):
        self.editor_id = editor_id
        self.piece_of_news_header = piece_of_news_header
        self.editor = editor
        self.content = content
        self.send_time = send_time

    def get_editor_id(self):
        return self.editor_id

    def get_piece_of_news_header(self):
        return self.piece_of_news_header

    def get_editor(self):
        return self.editor

    def get_send_time(self):
        return self.send_time

    def get_content(self):
        return self.content