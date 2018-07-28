# coding: utf-8

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.utils import make_result
from config import config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config[config_name])
    db.init_app(app)

    from app.match import match as match_blueprint
    app.register_blueprint(match_blueprint)
    ma.init_app(app)
    return app
