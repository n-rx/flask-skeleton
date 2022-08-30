import os.path
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Config(object):
    BUILD_MODE = os.getenv("BUILD_MODE")
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    CSRF_ENABLED = True
    DB_STATUS = bool(os.getenv("DB_STATUS"))


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQL = os.getenv("DEV_DB")


class DockerConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQL = os.getenv("DOCKER_DB")



class TestingConfig(Config):
    TESTING = True
    SQL = os.getenv("TEST_DB")


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SQL = os.getenv('PROD_DB')
