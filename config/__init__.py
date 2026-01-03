import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', '3306'))
    DB_NAME = os.getenv('DB_NAME', 'ai_chatbot_db')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_POOL_SIZE = int(os.getenv('DB_POOL_SIZE', '10'))
    DB_MAX_OVERFLOW = int(os.getenv('DB_MAX_OVERFLOW', '20'))
    DB_POOL_TIMEOUT = int(os.getenv('DB_POOL_TIMEOUT', '30'))
    DB_POOL_RECYCLE = int(os.getenv('DB_POOL_RECYCLE', '3600'))
    
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', '')
    
    LLM_API_ENDPOINT = os.getenv('LLM_API_ENDPOINT', 'https://api.openai.com/v1')
    LLM_API_KEY = os.getenv('LLM_API_KEY', '')
    LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-3.5-turbo')
    LLM_MAX_TOKENS = int(os.getenv('LLM_MAX_TOKENS', '1000'))
    LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', '0.7'))
    
    MAX_UPLOAD_SIZE = int(os.getenv('MAX_UPLOAD_SIZE', '10485760'))
    ALLOWED_EXTENSIONS = set(os.getenv('ALLOWED_EXTENSIONS', 'txt,pdf,doc,docx').split(','))
    
    @classmethod
    def get_database_uri(cls):
        return f"mysql+pymysql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DB_NAME = 'ai_chatbot_test_db'


config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    return config_by_name.get(config_name, DevelopmentConfig)
