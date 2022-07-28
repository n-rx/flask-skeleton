from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy import create_engine

import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']

    db.init_app(app)
    app.e = create_engine(app.config['SQL'], pool_size=5, pool_recycle=6)

    from IAPI.api.Views.testAPI import test_api
    app.register_blueprint(test_api)

    return app
