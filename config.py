import os
class Config:
    #SQLAlchemy ur
    SECRET_KEY=os.environ.get('SECRET_KEY')


    

class ProdConfig(Config):
    pass


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