

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class BidHeadersStatus(db.Model):
    __tablename__ = 'BidHeadersStatus'

    bidHeader_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    bidGenre = Column(String)  # Adjust the data type as needed
    bidHeader = Column(String)
    bidStartTime = Column(DateTime)
    lastEditedTime = Column(DateTime)
    isSold = Column(Boolean)  # Indicates whether the bid is mutually agreed upon (sold)

    # Define any additional relationships or constraints here if needed
