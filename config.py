"""Configuration module for Sentiment Analysis Dashboard."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    
    # Model settings
    MODEL_NAME = os.getenv('MODEL_NAME', 'distilbert-base-uncased-finetuned-sst-2-english')
    DEVICE = os.getenv('DEVICE', 'cpu')
    
    # Application settings
    APP_TITLE = 'Sentiment Analysis Dashboard for Social Media Trends'
    APP_DESCRIPTION = 'An advanced NLP dashboard for analyzing real-time public sentiment.'
    APP_VERSION = '1.0.0'
    
    # Data processing
    MAX_TWEETS = int(os.getenv('MAX_TWEETS_TO_FETCH', 100))
    MIN_TWEET_LENGTH = int(os.getenv('MIN_TWEET_LENGTH', 10))
    
    # Cache settings
    ENABLE_CACHE = os.getenv('ENABLE_CACHE', 'true').lower() == 'true'
    CACHE_EXPIRY_HOURS = int(os.getenv('CACHE_EXPIRY_HOURS', 24))

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True

def get_config(env=None):
    """Get configuration based on environment."""
    if env is None:
        env = os.getenv('ENVIRONMENT', 'development')
    
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
    }
    
    return config_map.get(env, DevelopmentConfig)
