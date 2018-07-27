# coding=utf-8
from flask import Blueprint

match = Blueprint('match', __name__)

import app.match.forms, app.match.views
