import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postinLent0d@localhost/db_BGEFv4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False