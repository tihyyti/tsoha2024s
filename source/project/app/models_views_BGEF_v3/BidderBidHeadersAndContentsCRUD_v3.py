
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
"""
# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class BidderBidHeadersAndContentsCRUD(db.Model):
    __tablename__ = 'BidderBidHeadersAndContentsCRUD'

    bidHeader_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    bidGenre = Column(String)  # Adjust the data type as needed
    bidHeader = Column(String)
    bidContent = Column(String)
    dealStatus = Column(String)  # Agreed or Open (adjust data type as needed)

    # Define any additional relationships or constraints here if needed
"""

class GearBundle(db.Model):
    __tablename__ = 'gear_bundle'

    id = db.Column(db.Integer, primary_key=True)
    dealStatus = Column(String)
    bundleName = db.Column(db.String(80), nullable=False)
    bundleGenre = Column(String)
    bundleContent = Column(String)
    price = db.Column(db.Float, nullable=False)
    user_id = Column(Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

     # Define any additional relationships or constraints here if needed
