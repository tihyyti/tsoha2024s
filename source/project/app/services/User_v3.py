
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Flask User CRUD-Service

class UserService:
    @staticmethod
    def create_user(userName, password):
        new_user = User(userName=userName, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, **kwargs):
        user = User.query.get(user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
