from api.config import Config
from api.dbconnection import urls


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = urls["testing"]


