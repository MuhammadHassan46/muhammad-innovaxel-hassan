import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'computerengineeringsession21'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://url_user:hassan@localhost/url_shortener'
    SQLALCHEMY_TRACK_MODIFICATIONS = False