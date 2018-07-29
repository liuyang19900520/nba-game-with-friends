# coding=utf-8
from app.models import AthleteBasic, RatingOverallOutsideScoringSchema, RatingOverallOutsideScoring


def first_round(athlete_id, *position):
    print(athlete_id)
    athlete = AthleteBasic.query.filter_by(athlete_id=athlete_id).first()

    if position == 'c':
        position_param = athlete.c_adaptability
    elif position == 'pf':
        position_param = athlete.pf_adaptability
    elif position == 'sf':
        position_param = athlete.sf_adaptability
    elif position == 'sg':
        position_param = athlete.sg_adaptability
    elif position == 'pg':
        position_param = athlete.pg_adaptability

    outside = RatingOverallOutsideScoring.query.filter_by(athlete_id=athlete_id).first()





    print(outside)
    outputSchema = RatingOverallOutsideScoringSchema()
    output = outputSchema.dump(outside).data
    return output
