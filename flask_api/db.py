from flask_sqlalchemy import SQLAlchemy
from flask_api.models.base_model import metadata

database = SQLAlchemy(metadata=metadata)

