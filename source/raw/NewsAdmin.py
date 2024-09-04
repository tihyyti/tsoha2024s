from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class NewsAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    startedBy = db.Column(db.Integer)
    genre = db.Column(db.Integer)
    header = db.Column(db.String(255))
    numberOfPieceOfNewsContents = db.Column(db.Integer, default=3)
    started = db.Column(db.DateTime, default=datetime.utcnow)

    def get_initiator(self):
        return self.startedBy

    def set_initiator(self, startedBy):
        self.startedBy = startedBy

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header

    def get_number_of_piece_of_news_contents(self):
        return self.numberOfPieceOfNewsContents

    def set_number_of_piece_of_news_contents(self, numberOfPieceOfNewsContents):
        self.numberOfPieceOfNewsContents = numberOfPieceOfNewsContents

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)