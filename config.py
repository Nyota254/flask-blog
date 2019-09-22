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
    DEBUG = True

configurations = {
    "production":ProdConfig,
    "development":DevConfig
}