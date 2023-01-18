from flask_api.app import create_app
from flask_api.db import database


def generate_metadata():
    app = create_app()
    return database.metadata
