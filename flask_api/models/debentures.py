from flask_api.models.base_model import Base, Column
import sqlalchemy as db

# TODO : FIX EVERY DEBENTURE RELATED (SCHEMA AND ENDPOINTS.)
class Debentures(Base):

    __tablename__ = "debentures"
    codigo_ativo = Column(db.String(30), primary_key=True)
    data_referencia = Column(db.Date, primary_key=True)

    pu = Column(db.Float, nullable=True)
    grupo = Column(db.String)
    duration = Column(db.Integer, nullable=True)
    taxa_indicativa = Column(db.Float)
    percentual_taxa = Column(db.String)
    precification_method = Column(db.String)

    data_vencimento = Column(db.Date)
    data_finalizado = Column(db.Date)
    taxa_compra = Column(db.Float, nullable=True)
    taxa_venda = Column(db.Float, nullable=True)
    desvio_padrao = Column(db.Float)
    val_min_intervalo = Column(db.Float)
    val_max_intervalo = Column(db.Float)
    percent_pu_par = Column(db.Float, nullable=True)
    percent_reune = Column(db.Float, nullable=True)
    emissor = Column(db.String)
    referencia_ntnb = Column(db.Date, nullable=True)
