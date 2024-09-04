
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class BidderGearList(db.Model):
    __tablename__ = 'BidderGearList'

    gear_id = Column(Integer, primary_key=True)
    gearGroup = Column(String)  # Adjust the data type as needed
    gearBrand = Column(String)
    gearCode = Column(Integer)
    gearStatus = Column(Integer)  # Adjust the data type as needed
    gearName = Column(String)
    amountOffered = Column(Float)  # Adjust the data type as needed
    gearImage_link = Column(String)  # Link to gear image (adjust data type as needed)
    sound_link = Column(String)  # Link to sound sample (adjust data type as needed)
    lastEditedTime = Column(DateTime)

    # Define any additional relationships or constraints here if needed
