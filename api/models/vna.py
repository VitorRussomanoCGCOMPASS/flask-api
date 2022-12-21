from api.models.base_model import Base, Column
import sqlalchemy as db


class VNA(Base):
    """
    Attributes
    ----------
    __tablename__ = "vna_anbima"

    Primary keys
    -----------
    data_referencia : Column(db.Date)

    codigo_selic: Column(db.Integer)

    Others
    ------
    tipo_titulo: Column(db.String)
    index: Column(db.Float)
    tipo_correcao: Column(db.String)
    data_validade: Column(db.Date)
    vna: Column(db.Float)

    Relationships
    --------------
    None


    Methods
    -------

    """

    __tablename__ = "anbima_vna"

    data_referencia = Column(db.Date, primary_key=True)
    tipo_titulo = Column(db.String(50))
    codigo_selic = Column(db.Integer, primary_key=True)
    index = Column(db.Float)
    tipo_correcao = Column(db.String)
    data_validade = Column(db.Date)
    vna = Column(db.Float)
