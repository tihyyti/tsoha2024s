
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InitialBidderBids(Base):
    __tablename__ = 'InitialBidderBids'

    bidHeader_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    bidGenre = Column(String)  # Adjust the data type as needed
    bidHeader = Column(String)
    bidStartTime = Column(DateTime)
    bidContent = Column(String)

    # Define any additional relationships or constraints here if needed
