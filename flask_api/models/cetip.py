import sqlalchemy as db

from flask_api.models.base_model import Base
from sqlalchemy import null

class CetipBase(Base):

    __abstract__  = True
    type = db.Column(db.String(3))
    issuer = db.Column(db.String,nullable=True)
    instrument_code = db.Column(db.String(50),primary_key=True)
    price_max = db.Column(db.Float)
    price_mean = db.Column(db.Float)
    price_min = db.Column(db.Float)
    rate_max = db.Column(db.Float,nullable=True)
    rate_mean = db.Column(db.Float,nullable=True)
    rate_min = db.Column(db.Float,nullable=True)
    quantity = db.Column(db.Float)
    nof_trades = db.Column(db.Float)
    financial_vol = db.Column(db.Float)
    last_price = db.Column(db.Float)
    last_rate = db.Column(db.Float,nullable=True)
    last_trade_source = db.Column(db.Float)
    last_trade_closing_time = db.Column(db.Float)
    last_trade_settlement_date = db.Column(db.Float)
    date = db.Column(db.Date,primary_key=True)


class Cetip(CetipBase):
    __tablename__ =  "cetip"

class StageCetip(CetipBase):
    __tablename__ = "stage_" + Cetip.__tablename__

    rate_max = db.Column(db.Float,nullable=True,default=null())
    rate_mean = db.Column(db.Float,nullable=True,default=null())
    rate_min = db.Column(db.Float,nullable=True,default=null())
    last_rate = db.Column(db.Float,nullable=True,default=null())
