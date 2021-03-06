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


class RatingOverallOutsideScoring(db.Model):
    athlete_id = db.Column(db.Integer, primary_key=True)
    open_shot_mid = db.Column(db.Integer)
    open_shot_3pt = db.Column(db.Integer)
    shot_iq = db.Column(db.Integer)
    off_dribble_shot_mid = db.Column(db.Integer)
    off_dribble_shot_3pt = db.Column(db.Integer)
    free_throw = db.Column(db.Integer)
    contested_shot_mid = db.Column(db.Integer)
    contested_shot_3pt = db.Column(db.Integer)
    offensive_consistency = db.Column(db.Integer)

    def __repr__(self):
        return '<OutsideScoring %f>' % ((
                                                self.open_shot_mid + self.open_shot_3pt + self.shot_iq
                                                + self.off_dribble_shot_mid + self.off_dribble_shot_3pt
                                                + self.free_throw + self.contested_shot_mid + self.contested_shot_3pt + self.offensive_consistency) / 9)


class RatingOverallOutsideScoringSchema(ma.ModelSchema):
    class Meta:
        model = RatingOverallOutsideScoring

    # Again, add an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        return data
