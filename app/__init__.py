# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config[config_name])
    db.init_app(app)

    from app.match import match as match_blueprint
    app.register_blueprint(match_blueprint)

    return app
