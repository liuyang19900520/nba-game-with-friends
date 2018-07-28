# coding=utf-8
from flask import request
from flask_restful import Resource

from app.match.athlete_stats import first_round
from ..utils import make_result


class Test(Resource):

    def post(self):
        athlete_id=request.form['athlete_id']
        round1 = first_round(athlete_id)
        return make_result(data=round1)
