class Config(object):
    TESTING = False
    SECRET_KEY = "need_to_be_changed"
    SQL = "postgresql://postgres:postgres@localhost:5432/postgres"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/postgres"
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQL = "postgresql://postgres:postgres@localhost:5432/api_testing"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/api_testing"
