
from api.dbconnection import urls

class Config(object):
    SQLALCHEMY_DATABASE_URI = urls["localdev"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"Title":"API.v1"}