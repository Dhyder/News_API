import os

class Config:
    '''
    Config parent class
    '''
    NEWS_API_KEY = os.environ.get('HEADLINES_API_KEY')
    HEADLINES_API_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    EVERYTHING_API_BASE_URL = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    SOURCES_API_BASE_URL = "https://newsapi.org/v2/sources?category={}&apiKey={}"
    SOURCES_ARTICLE_API_BASE_URL = "https://newsapi.org/v2/top-headlines?id={}&apiKey={}"
class ProdConfig(Config):
    '''
    Production config child class
    '''
    pass

class DevConfig(Config):
    '''
    Development config child class
    '''
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}