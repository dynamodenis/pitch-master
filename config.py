class Config:
    pass
    

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