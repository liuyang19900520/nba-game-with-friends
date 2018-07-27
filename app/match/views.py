# coding=utf-8
from . import match
from flask import Flask
from ..models import AthleteBasic


@match.route("/")
def hello():
    query_all = AthleteBasic.query.all()

    return query_all
