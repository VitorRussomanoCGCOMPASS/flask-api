from flask_api.models.base_model import Base
import sqlalchemy as db


class DebenturesBase(Base):
    __abstract__ = True
    codigo_ativo = db.Column(db.String(30), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)

    grupo = db.Column(db.String)
    taxa_indicativa = db.Column(db.Float)
    percentual_taxa = db.Column(db.String)

    data_vencimento = db.Column(db.Date)
    data_finalizado = db.Column(db.Date)

    desvio_padrao = db.Column(db.Float)
    val_min_intervalo = db.Column(db.Float)
    val_max_intervalo = db.Column(db.Float)

    emissor = db.Column(db.String)
    pu = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    taxa_compra = db.Column(db.Float, nullable=True)
    taxa_venda = db.Column(db.Float, nullable=True)
    percent_pu_par = db.Column(db.Float, nullable=True)
    percent_reune = db.Column(db.VARCHAR, nullable=True)
    referencia_ntnb = db.Column(db.Date, nullable=True)


class Debentures(DebenturesBase):
    __tablename__ = "debentures"
    percent_reune = db.Column(db.Float, nullable=True)

class StageDebentures(DebenturesBase):
    __tablename__ = "stage_" + Debentures.__tablename__

    emissor = db.Column(db.String)
    data_finalizado = db.Column(db.String(50))
    data_vencimento = db.Column(db.String(50))


