from api.models.base_model import Base, Column
from sqlalchemy.orm import relationship
import sqlalchemy as db


class HolidayCalendars(Base):
    __tablename__ = "holidays_calendars"
    id = Column(db.Integer, autoincrement=True, primary_key=True)

    calendar = Column(db.String(50))
    holidays = relationship("Holidays")


class Holidays(Base):
    __tablename__ = "holidays"
    date = Column(db.Date, primary_key=True)
    calendar_id = Column(
        db.Integer, db.ForeignKey("holidays_calendars.id"), primary_key=True
    )
