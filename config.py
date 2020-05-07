import os
from flask_mail import Mail
class Config:
    #SQLAlchemy ur
    SECRET_KEY=os.environ.get('SECRET_KEY')
    #emailconfiguration
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/pitch_master'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/pitch_test'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}