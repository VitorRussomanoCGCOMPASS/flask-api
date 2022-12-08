from api.models.base_model import Base, Column
import sqlalchemy as db
from sqlalchemy import extract
from sqlalchemy.ext.hybrid import hybrid_property


class EventLog(Base):
    __tablename__ = "eventlog"
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    asctime = Column(db.DateTime)
    name = Column(db.String(50))
    funcName = Column(db.String(50))
    levelname = Column(db.String(50))
    module = Column(db.String(50))
    lineno = Column(db.Float)
    thread = Column(db.Float)
    threadName = Column(db.String(50))
    message = Column(db.String)
