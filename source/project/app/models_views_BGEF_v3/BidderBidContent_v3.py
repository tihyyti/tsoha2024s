
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class BidderBidContent(db.Model):
    __tablename__ = 'BidderBidContent'

    bidHeader_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    bidGenre = Column(String)  # Adjust the data type as needed
    bidHeader = Column(String)
    bidContent = Column(String)

    # Define any additional relationships or constraints here if needed