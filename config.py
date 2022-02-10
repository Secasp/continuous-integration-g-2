import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://user:password@host/db?auth_plugin=mysql_native_password"

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
