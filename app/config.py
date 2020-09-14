class Config:
    '''
    General configuration parent class
    '''
    pass
   
    
    # SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?language={}&apiKey={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    HEADLINE_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    config_options = {
'development':DevConfig,
'production':ProdConfig
}
