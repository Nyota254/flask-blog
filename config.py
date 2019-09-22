import os
class Config:
    '''
    General configuration settings
    '''
    pass

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    pass

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://kevin:1234@localhost/flaskblog"
    DEBUG = True

configurations = {
    "production":ProdConfig,
    "development":DevConfig
}