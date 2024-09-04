
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class UserRolesAndLastBidHeaders(db.Model):
    __tablename__ = 'AdminUserRolesAndLastBidHeaders'

    user_id = Column(Integer, primary_key=True)
    userName = Column(String, nullable=False)
    userRole = Column(String)  # Adjust the data type as needed
    lastBidHeader = Column(String)  # Adjust the data type as needed
    lastBidStartTime = Column(DateTime)  # Adjust the data type as needed

    # Define any additional relationships or constraints here if needed