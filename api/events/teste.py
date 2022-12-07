from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker

from api.dbconnection import urls
from api.models.base_model import database
from api.models.sector import SectorEntry


#   with scheduler.app.app_context():
def scheduled_task():
    print("ok")

""" 

Alternatively (and probably the best solution) would be to actually set up a thread-local scoped SQLAlchemy session instead of relying on Flask-SQLAlchemy's request context.

>>> from sqlalchemy.orm import scoped_session
>>> from sqlalchemy.orm import sessionmaker

>>> session_factory = sessionmaker(bind=some_engine)
>>> Session = scoped_session(session_factory)

 """
