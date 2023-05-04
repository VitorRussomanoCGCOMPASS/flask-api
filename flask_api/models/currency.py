from flask_api.models.base_model import Base, Column
import sqlalchemy as db
from sqlalchemy.orm import relationship


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(db.Integer, autoincrement=True, primary_key=True)
    currency = Column(db.String)
    
    exchange_rates = relationship("ExchangeRates")

class ExchangeRatesBase(Base):
    __abstract__ = True

    date = Column(db.Date, primary_key=True)
    value = Column(db.Float)

class ExchangeRates(ExchangeRatesBase):
    __tablename__ = "exchange_rates"

    domestic_id = Column(db.Integer, db.ForeignKey("currencies.id"), primary_key=True)
    foreign_id = Column(db.Integer, db.ForeignKey("currencies.id"), primary_key=True)

    domestic_currency = relationship(
        "Currency", primaryjoin="ExchangeRate.domestic_id == Currency.id"
    )
    foreign_currency = relationship(
        "Currency", primaryjoin="ExchangeRate.foreign_id == Currency.id"
    )

class StageExchangeRates(ExchangeRatesBase):
    __tablename__ = "stage_" + ExchangeRates.__tablename__

    domestic_id = Column(db.Integer, primary_key=True)
    foreign_id = Column(db.Integer, primary_key=True)

