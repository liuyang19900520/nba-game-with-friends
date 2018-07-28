# coding=utf-8

from flask_restful import Resource, fields, marshal_with

from ..models import AthleteBasic, AthleteBasicSchema
from ..utils import make_result


class Test(Resource):

    def get(self):
        athlete_basic_list = AthleteBasic.query.all()
        print(athlete_basic_list)



        aa = AthleteBasicSchema()
        output = aa.dump(list(athlete_basic_list)).data

        return make_result(data=output)

# @match.route("/")
# def hello():
#     query_all = AthleteBasic.query.all()
#     temp = []
#     for x in query_all:
#         temp.append(x.json)
#
#     return jsonify(objects=temp)
