from marshmallow import post_dump

from . import db
from . import ma


class AthleteBasic(db.Model):
    athlete_id = db.Column(db.Integer, primary_key=True)
    athlete_name = db.Column(db.String(64), nullable=False)
    c_adaptability = db.Column(db.Integer)
    pf_adaptability = db.Column(db.Integer)
    sf_adaptability = db.Column(db.Integer)
    sg_adaptability = db.Column(db.Integer)
    pg_adaptability = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.athlete_name


class AthleteBasicSchema(ma.ModelSchema):
    class Meta:
        model = AthleteBasic

    # Again, add an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        return data


