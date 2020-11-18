import os

class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key'
    POSTGRES = {
    'user': 'postgres',
    'pw': '1',
    'db': 'loan_inc',
    'host': 'localhost',
    'port': '5433',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    # "postgresql://postgres:1@localhost:5433/loan_inc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False