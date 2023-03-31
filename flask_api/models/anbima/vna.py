from flask_api.models.base_model import Base
import sqlalchemy as db


class VNABase(Base):
    __abstract__ = True

    data_referencia = db.Column(db.Date, primary_key=True)
    tipo_titulo = db.Column(db.String(50))
    codigo_selic = db.Column(db.String(6), primary_key=True)
    index = db.Column(db.Float)
    tipo_correcao = db.Column(db.String)
    data_validade = db.Column(db.Date)
    vna = db.Column(db.Float)


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

    __tablename__ = "vna_anbima"


class TempVNA(VNABase):
    __tablename__ = "temp_" + VNA.__tablename__
