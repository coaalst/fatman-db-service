import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('ENTRY_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'fatman.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
