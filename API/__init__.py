from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from config import Config

import config
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    if Config.BUILD_MODE == "prod":
        app_settings = config.ProductionConfig
    elif Config.BUILD_MODE == "docker":
        app_settings = config.DockerConfig
    elif Config.BUILD_MODE == 'testing':
        app_settings = config.TestingConfig
    else:
        app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQL']

    db.init_app(app)
    app.e = create_engine(app.config['SQL'], pool_size=5, pool_recycle=6)
    from API.test_api.Views.testAPI import test_api
    app.register_blueprint(test_api)

    return app
