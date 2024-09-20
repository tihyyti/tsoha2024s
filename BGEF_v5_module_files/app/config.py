import os
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import psycopg2
#
# app/config.py

class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postinLent0@localhost:5000/dbBGEF_v5')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
    'postgresql://postgres:postinLent0@localhost:5432/dbBGEF_v5')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENVIRONMENT = "development"
    FLASK_APP = "app"
    FLASK_DEBUG = True
    SECRET_KEY = "0b6a3f3205bd3b63b803d815c938a981"