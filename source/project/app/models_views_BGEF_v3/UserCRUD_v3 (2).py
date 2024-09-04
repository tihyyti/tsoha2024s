
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class AdminBidderCRUD(db.Model):
    __tablename__ = 'UserCRUD'

    user_id = Column(Integer, primary_key=True)
    userName = Column(String, nullable=False)
    userRole = Column(String)  # Adjust the data type as needed
    isBlocked = Column(Boolean)

    # Define any additional relationships or constraints here if needed
