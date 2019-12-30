import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""
Config that the flask server is initialised with.
"""
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'a-very-secret-secret'

    """
    Debugging and testing
    """
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
