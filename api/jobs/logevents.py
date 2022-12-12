""" Pushing the days log events to sql  """
import json

from api.schemas.eventlog import EventLogSchema

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from api.dbconnection import urls


def upload_logevents():
    
    some_engine = create_engine(urls["localdev"])

    session_factory = sessionmaker(bind=some_engine)

    Session = scoped_session(session_factory)

    eventlogs = []
    with open("api/events/eventslog.json") as file:
        for line in file:
            eventlogs.append(json.loads(line))

    eventlog_schema = EventLogSchema()
    eventlog_objs = eventlog_schema.load(eventlogs, many=True)
    with Session() as session:
        session.add_all(eventlog_objs)
        session.commit()


if __name__ == "__main__":
    upload_logevents()
