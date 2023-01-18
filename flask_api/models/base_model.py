# from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)  

# database = SQLAlchemy(model_class=Base)




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


