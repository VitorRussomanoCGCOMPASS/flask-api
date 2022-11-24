from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()
database = SQLAlchemy(model_class=Base)


def Column(*args, **kwargs):
    """
    Creates a wrapper for the columns.
    With the default arguments being Nullable=False.
    Instead of the Nullable=True in sqlalchemy.

    Returns
    -------
    db.Column
    """
    kwargs.setdefault("nullable", False)
    return db.Column(*args, **kwargs)


