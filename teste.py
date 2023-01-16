""" 
Created models can be used outside of the Flask context via a Session. For example:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from api.models.base_model import metadata
from api.models.currency import Currency
from api.config import Config

engine =create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
currencies = session.query(Currency).all()
session.close()


