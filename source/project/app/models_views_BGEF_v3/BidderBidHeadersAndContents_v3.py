
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class BidderBidHeadersAndContents(db.Model):
    __tablename__ = 'BidderBidHeadersAndContents'

    bidHeader_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    bidGenre = Column(String)
    bidHeader = Column(String)
    bidContent = Column(String)
    dealStatus = Column(String)  # Agreed or Open (adjust data type as needed)

    # Define any additional relationships or constraints here if needed
