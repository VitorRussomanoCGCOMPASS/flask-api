from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy import null


class VNABase(Base):

    __abstract__ = True
    data_referencia = db.Column(db.Date, primary_key=True)


class VNA(VNABase):
    """
    Attributes
    ----------
    __tablename__ = "vna_anbima"

    Primary keys
    -----------
    data_referencia : db.Column(db.Date)

    codigo_selic: db.Column(db.Integer)

    Others
    ------
    tipo_titulo: db.Column(db.String)
    index: db.Column(db.Float)
    tipo_correcao: db.Column(db.String)
    data_validade: db.Column(db.Date)
    vna: db.Column(db.Float)

    Relationships
    --------------
    None


    Methods
    -------

    """

    __tablename__ = "anbima_vna"

    data_referencia = db.Column(db.Date, primary_key=True)

    tipo_titulo = db.Column(db.String(50))
    codigo_selic = db.Column(db.String(6), primary_key=True)
    index = db.Column(db.Float)
    tipo_correcao = db.Column(db.String)
    data_validade = db.Column(db.Date)
    vna = db.Column(db.Float)


class StageVNA(VNABase):
    __tablename__ = "stage_" + VNA.__tablename__

    rowid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulos = db.Column(db.JSON)

    tipo_titulo = db.Column(db.String(50), nullable=True, default=null())
    codigo_selic = db.Column(db.String(6), nullable=True, default=null())
    index = db.Column(db.Float, nullable=True, default=null())
    tipo_correcao = db.Column(db.String, nullable=True, default=null())
    data_validade = db.Column(db.Date, nullable=True, default=null())
    vna = db.Column(db.Float, nullable=True, default=null())

