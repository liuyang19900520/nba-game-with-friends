# coding=utf-8
from app.models import AthleteBasic, AthleteBasicSchema


def first_round(athlete_id):
    print(athlete_id)
    athlete = AthleteBasic.query.filter_by(athlete_id=athlete_id).first()

    print(athlete)
    athleteSchema = AthleteBasicSchema()
    output = athleteSchema.dump(athlete).data
    return output
