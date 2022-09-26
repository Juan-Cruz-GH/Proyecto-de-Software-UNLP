from distutils.command.config import config


class Config(object):
    """Base configuration."""
    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    """Production configuration."""
    pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DB_SERVER = "localhost"
    DB_DATABASE = "proyecto_db"
    DB_USER = "postgres"
    DB_PASSWORD = "proyecto"
    DB_PORT = "5432"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}"

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig
}