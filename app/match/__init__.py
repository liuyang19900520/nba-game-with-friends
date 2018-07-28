# coding=utf-8
from flask import Blueprint
from flask_restful import Api
from .views import Test

match = Blueprint('match', __name__)

resource = Api(match)
resource.add_resource(Test, "/")  # 设置路由