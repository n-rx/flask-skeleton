import config
from flask import Flask


def create_app():
    app = Flask(__name__)
    app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)
    from IAPI.api.Views.testAPI import test_api
    app.register_blueprint(test_api)

    return app
