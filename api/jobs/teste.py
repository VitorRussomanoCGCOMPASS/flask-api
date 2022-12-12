from flask_apscheduler import scheduler
from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker

from api.dbconnection import urls
from api.models.base_model import database
from api.models.sector import SectorEntry


from api.models.eventlog import EventLog

some_engine = create_engine(url=urls["localdev"])

session_factory = sessionmaker(bind=some_engine)


Session = scoped_session(session_factory)
import datetime

today = datetime.datetime.today()
EventLog.query.filter(EventLog.asctime_date==today)


def scheduled_task():
    with Session() as session:
        print(session.query(SectorEntry).all())





