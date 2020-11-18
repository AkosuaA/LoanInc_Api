import os

class Config(object):

    #format for db uri is "postgresql://user:password@host:port/db_name"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    "postgresql://postgres:1@localhost:5433/loan_inc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False