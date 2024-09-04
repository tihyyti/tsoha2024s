

from typing import List
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

class NewsGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PieceOfNewsHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    started_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PieceOfNewsContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@dataclass
class User:
    userName: str
    password: str = ""
    newsGenres: List['NewsGenre'] = None
    pieceOfNewsHeaders: List['PieceOfNewsHeader'] = None
    pieceOfNewsContents: List['PieceOfNewsContent'] = None

    def get_user_name(self) -> str:
        return self.userName

    def get_news_genres(self) -> List['NewsGenre']:
        if self.newsGenres is None:
            self.newsGenres = []
        return self.newsGenres

    def add_news_genre(self, news_genre: 'NewsGenre') -> List['NewsGenre']:
        if self.newsGenres is None:
            self.newsGenres = []
        self.newsGenres.append(news_genre)
        return self.newsGenres

    def del_piece_of_news_header(self, news_genre: 'NewsGenre') -> None:
        if self.newsGenres is not None:
            self.newsGenres.remove(news_genre)

    def get_piece_of_news_headers(self) -> List['PieceOfNewsHeader']:
        if self.pieceOfNewsHeaders is None:
            self.pieceOfNewsHeaders = []
        return self.pieceOfNewsHeaders

    def add_piece_of_news_header(self, pieceOfNewsHeader: 'PieceOfNewsHeader') -> List['PieceOfNewsHeader']:
        if self.pieceOfNewsHeaders is None:
            self.pieceOfNewsHeaders = []
        self.pieceOfNewsHeaders.append(pieceOfNewsHeader)
        return self.pieceOfNewsHeaders

    # getPieceOfNewsContents()
    def get_piece_of_news_contents(self):
      if not self.piece_of_news_contents:
        self.piece_of_news_contents = []
    return self.piece_of_news_contents

    # addPieceOfNewsContent(PieceOfNewsContent pieceOfNewsContent)
    def add_piece_of_news_content(self, piece_of_news_content):
      if not self.piece_of_news_contents:
          self.piece_of_news_contents = []
      self.piece_of_news_contents.append(piece_of_news_content)
      return self.piece_of_news_contents

    # delPieceOfNewsContent(PieceOfNewsContent pieceOfNewsContent)
    def del_piece_of_news_content(self, piece_of_news_content):
      if not self.piece_of_news_contents:
          return
      self.piece_of_news_contents.remove(piece_of_news_content)

'''  '''
'''   Translate following Java methods in Spring Boot Framework into Python 3.12 in Flask: '''
'''  '''
'''     public User() { '''
'''     } '''
'''  '''
'''     public User(String userName) { '''
'''         this.userName = userName; '''
'''         this.password = ""; '''
'''  '''
'''         List<NewsGenre> newsGenres = new ArrayList<>(); '''
'''         List<PieceOfNewsHeader> pieceOfNewsHeaders = new ArrayList<>(); '''
'''         List<PieceOfNewsContent> pieceOfNewsContents = new ArrayList<>(); '''
'''     } '''
'''  '''
'''     public User(String userName, String password) { '''
'''         this.userName = userName; '''
'''         this.password = password; '''
'''  '''
'''         List<NewsGenre> newsGenres = new ArrayList<>(); '''
'''         List<PieceOfNewsHeader> pieceOfNewsHeaders = new ArrayList<>(); '''
'''         List<PieceOfNewsContent> pieceOfNewsContents = new ArrayList<>(); '''
'''     } '''
'''  '''
'''     public String getUserName() { '''
'''         return userName; '''
'''     } '''
'''  '''
'''   if __name__ == '__main__': '''
'''     db.create_all() '''
'''     app.run(debug=True) '''
'''  '''
'''  '''
'''  '''
'''  '''





