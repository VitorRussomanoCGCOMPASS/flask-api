from api.models.base_model import Base, Column
from sqlalchemy.orm import relationship
import sqlalchemy as db



class HolidayCalendars(Base):
    __tablename__ = "holidays_calendars"
    id = Column(db.Integer, autoincrement=True, primary_key=True)
    calendar = Column(db.String(50))
    holidays = relationship("Holidays",back_populates='calendar')


class Holidays(Base):
    __tablename__ = "holidays"
    date = Column(db.Date, primary_key=True)
    calendar = relationship("HolidayCalendars")
    calendar_id = Column(
        db.Integer, db.ForeignKey("holidays_calendars.id"), autoincrement=True,primary_key=True
    )



