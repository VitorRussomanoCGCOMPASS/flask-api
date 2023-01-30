from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship


class Funds(Base):
    __tablename__ = "funds"
    
    britech_id = db.Column(db.Integer, primary_key=True,autoincrement=False)
    cnpj = db.Column(db.String)
    apelido = db.Column(db.String)
    cotista_id = db.Column(db.Integer,nullable=True)
    inception_date = db.Column(db.Date)

    values = relationship("FundsValues")


class FundsValues(Base):
    __tablename__ = "funds_values"

    date = db.Column(db.Date, primary_key=True)
    funds_id = db.Column(db.Integer, db.ForeignKey("funds.britech_id"), primary_key=True)
    cota = db.Column(db.Float)
