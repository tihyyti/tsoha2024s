from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

class UserRolesAuthorization(db.Model):
    __tablename__ = 'UserRolesAuthorization'

    user_id = Column(Integer, primary_key=True)
    userName = Column(String, nullable=False)
    selectedRole = Column(String)  # Adjust the data type as needed

    # Define any additional relationships or constraints here if needed