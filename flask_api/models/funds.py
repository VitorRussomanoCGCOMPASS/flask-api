from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship



class Funds(Base):
    __tablename__ = "funds"

    britech_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    cnpj = db.Column(db.String)
    apelido = db.Column(db.String)
    name = db.Column(db.String)
    type = db.Column(db.String)
    inception_date = db.Column(db.Date)
    closure_date = db.Column(db.Date)

    values = relationship("FundsValues")

class FundsValuesBase(Base):
    __abstract__ = True

    IdCarteira = db.Column(db.Integer, primary_key=True, autoincrement=False)
    Data = db.Column(db.Date, primary_key=True)
    CotaAbertura = db.Column(db.Float)
    CotaFechamento = db.Column(db.Float)
    CotaBruta = db.Column(db.Float)
    PLAbertura = db.Column(db.Float)
    PLFechamento = db.Column(db.Float)
    PatrimonioBruto = db.Column(db.Float)
    QuantidadeFechamento = db.Column(db.Float)
    AjustePL = db.Column(db.Float)
    CotaImportada =db.Column(db.String)
    CotaEx = db.Column(db.Float)
    CotaRendimento = db.Column(db.Float)
    ProventoAcumulado = db.Column(db.Float)
    IdSerieOffShore = db.Column(db.Integer)

class FundsValues(FundsValuesBase):
    __tablename__ = "funds_values"
    IdCarteira = db.Column(
        db.Integer, db.ForeignKey("funds.britech_id"), primary_key=True, autoincrement=False
    )

class TempFundsValues(FundsValuesBase):
    __tablename__ = "temp_" + FundsValues.__tablename__ 

