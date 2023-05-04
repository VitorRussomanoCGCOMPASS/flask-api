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


from flask_api.models.views import View
from sqlalchemy import select, func

class StageVNAView(Base):
    __table__ = View(
        "stage_anbima_vna_titulos" ,
        Base.metadata,
        select(
        StageVNA.data_referencia,
        func.JSON_VALUE(StageVNA.titulos, '$[0].tipo_titulo').label('tipo_titulo'),
        func.JSON_VALUE(StageVNA.titulos, '$[0].codigo_selic').label('codigo_selic'),
        func.JSON_VALUE(StageVNA.titulos, '$[0].index').label('index'),
        func.JSON_VALUE(StageVNA.titulos, '$[0].tipo_correcao').label('tipo_correcao'),
        func.JSON_VALUE(StageVNA.titulos, '$[0].data_validade').label('data_validade'),
        func.JSON_VALUE(StageVNA.titulos, '$[0].vna').label('vna'),
        )
    )

