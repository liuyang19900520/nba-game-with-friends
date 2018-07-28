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
        model=AthleteBasic

    # def to_json(self):
    #     return {
    #         'athlete_id': self.athlete_id,
    #         'athlete_name': self.athlete_name,
    #         'c_adaptability': self.c_adaptability,
    #         'pf_adaptability': self.pf_adaptability,
    #         'sf_adaptability': self.sf_adaptability,
    #         'sg_adaptability': self.sg_adaptability,
    #         'pg_adaptability': self.pg_adaptability
    #     }
    #
    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
