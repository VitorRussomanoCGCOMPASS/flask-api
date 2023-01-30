from flask_api.models.base_model import Base , Column
import sqlalchemy as db
from sqlalchemy.orm import relationship

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(db.Integer, autoincrement=True, primary_key=True)
    currency = Column(db.String)
    values = relationship("CurrencyValues", backref="currency")


class CurrencyValues(Base):
    __tablename__ = "currencies_values"

    date = Column(db.Date, primary_key=True)
    value = Column(db.Float)
    currency_id = Column(db.Integer, db.ForeignKey("currencies.id"), primary_key=True)


