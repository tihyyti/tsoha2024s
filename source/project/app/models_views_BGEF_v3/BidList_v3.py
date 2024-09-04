
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# the model for the BidList view

class BidList(db.Model):
    __tablename__ = 'BidList'
    id = db.Column(db.Integer, primary_key=True)
    initialBidder_id = db.Column(db.Integer)
    bidGenre_id = db.Column(db.Integer)
    bidTypeCode = db.Column(db.Integer)
    gearGroup_id = db.Column(db.Integer)
    numberOfBids = db.Column(db.Integer, nullable=False)
    bidHeaderText = db.Column(db.String(100), nullable=False)
    bidStartedTime = db.Column(db.DateTime, nullable=False)
    hdrEditedTime = db.Column(db.DateTime, nullable=False)
