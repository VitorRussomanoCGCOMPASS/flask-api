from flask_api.app import create_app
app = create_app()

from flask_api.db import database
database.metadata.tables