from flask_api.models.base_model import Base
import sqlalchemy as db


class DebenturesBase(Base):
    __abstract__ = True
    codigo_ativo = db.Column(db.String(30), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)

    pu = db.Column(db.Float, nullable=True)
    grupo = db.Column(db.String)
    duration = db.Column(db.Integer, nullable=True)
    taxa_indicativa = db.Column(db.Float)
    percentual_taxa = db.Column(db.String)

    data_vencimento = db.Column(db.Date)
    data_finalizado = db.Column(db.Date)
    taxa_compra = db.Column(db.Float, nullable=True)
    taxa_venda = db.Column(db.Float, nullable=True)
    desvio_padrao = db.Column(db.Float)
    val_min_intervalo = db.Column(db.Float)
    val_max_intervalo = db.Column(db.Float)
    percent_pu_par = db.Column(db.Float, nullable=True)
    percent_reune = db.Column(db.Float, nullable=True)
    emissor = db.Column(db.String)
    referencia_ntnb = db.Column(db.Date, nullable=True)


class Debentures(DebenturesBase):
    __tablename__ = "debentures"


class TempDebentures(DebenturesBase):
    __tablename__ = "temp_" + Debentures.__tablename__