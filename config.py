import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://matthew:J%40maica1992@dbserver/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
