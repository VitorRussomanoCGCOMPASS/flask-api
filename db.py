from flask_sqlalchemy import SQLAlchemy
from api.models.base_model import metadata

database = SQLAlchemy(metadata=metadata)

