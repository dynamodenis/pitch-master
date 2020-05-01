class Config:
    #SQLAlchemy ur
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/pitch_master'


    

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}