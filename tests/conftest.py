import pytest
import config
from IAPI import create_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import contextlib
from sqlalchemy import MetaData


@pytest.fixture
def app():
	app = create_app()
	app.test_client()
	app_settings = config.TestingConfig
	app.config.from_object(app_settings)
	app.e = create_engine(app.config['SQL'], pool_size=5, pool_recycle=6)

	db = SQLAlchemy(app)
	db.init_app(app)

	yield app


@pytest.fixture
def client(app):
	return app.test_client()
