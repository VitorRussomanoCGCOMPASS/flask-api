from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship


class Funds(Base):
    __tablename__ = "Funds"

    IdFundo = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.Integer)
    apelido = db.Column(db.String)
    IdCotista = db.Column(db.Integer)

    values = relationship("FundsValues")


class FundsValues(Base):
    __tablename__ = "Funds_values"

    date = db.Column(db.Date, primary_key=True)
    funds_id = db.Column(db.Integer, db.ForeignKey("funds.id"), primary_key=True)
    ValorCota = db.Column(db.Float)
