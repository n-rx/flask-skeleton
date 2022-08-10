class Config(object):
    TESTING = False
    SECRET_KEY = "need_to_be_changed"
    SQL = "postgresql://postgres:postgres@localhost:5432/postgres"
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQL = "postgresql://postgres:postgres@localhost:5432/postgres"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQL = "postgresql://postgres:postgres@localhost:5432/data"


class DockerConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQL = "postgresql://postgres:postgres@postgres:5432/data"


class TestingConfig(Config):
    TESTING = True
    SQL = "postgresql://postgres:postgres@localhost:5432/api_testing"
