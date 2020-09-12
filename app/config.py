class Config:
    '''
    General configuration parent class
    '''
    pass
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v1/articles?source=the-next-web&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'


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