class Config(object):
    TESTING = False
    SECRET_KEY = "need_to_be_changed"
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
