from flask_api.models.base_model import Base
import sqlalchemy as db


class CotistaOp(Base):

    __tablename__ = 'cotista_op'
    
    IdOperacao = db.Column(db.Integer, primary_key=True)
    IdCotista = db.Column(db.Integer)
    ApelidoCotista = db.Column(db.String)
    IdCarteira = db.Column(db.Integer)
    ApelidoCarteira = db.Column(db.String)
    CnpjCarteira = db.Column(db.String)
    ApelidoDistribuidor=db.Column(db.String,nullable=True)
    CnpjDistribuidor=db.Column(db.String,nullable=True)
    DataOperacao = db.Column(db.Date)
    DataRegistro = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    TipoOperacao = db.Column(db.Integer)
    DescricaoTipoOperacao = db.Column(db.String)
    ValorBruto = db.Column(db.Float)
    ValorLiquido = db.Column(db.Float)
    Quantidade = db.Column(db.Float)
    