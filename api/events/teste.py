from flask_apscheduler import scheduler
from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker

from api.dbconnection import urls
from api.models.base_model import database
from api.models.sector import SectorEntry

# A thread-local scoped SQLAlchemy session instead of relying on Flask-SQLAlchemy's request context.


some_engine = create_engine(url=urls["localdev"])

session_factory = sessionmaker(bind=some_engine)


Session = scoped_session(session_factory)


def scheduled_task():
    with Session() as session:
        print(session.query(SectorEntry).all())



