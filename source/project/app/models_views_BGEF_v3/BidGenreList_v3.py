
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# the model for the BidGenreList view

class BidGenreList(db.Model):
    __tablename__ = 'BidGenreList'

    id = db.Column(db.Integer, primary_key=True)
    bidGenreHeader = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer)
    latest = db.Column(db.DateTime)