from flask_api.models.base_model import Base, Column
import sqlalchemy as db
from sqlalchemy import null


class RendaFixaBase(Base):
    __abstract__ = True

    IdPosicao = db.Column(db.Integer, autoincrement=False, primary_key=True)
    DataHistorico = db.Column(db.VARCHAR)
    IdCliente = db.Column(db.Integer)
    NomeCliente = db.Column(db.String)
    ApelidoCliente = db.Column(db.String)
    IdTitulo = db.Column(db.Integer)
    TipoOperacao = db.Column(db.Integer)
    DataVencimento = db.Column(db.VARCHAR)
    QuantidadeInicial = db.Column(db.Float)
    Quantidade = db.Column(db.Float)
    QuantidadeBloqueada = db.Column(db.Float)
    QuantidadeDisponivel = db.Column(db.Float)
    DataOperacao = db.Column(db.VARCHAR)
    DataLiquidacao = db.Column(db.VARCHAR)
    PUOperacao = db.Column(db.Float)
    PUCurva = db.Column(db.Float)
    ValorCurva = db.Column(db.Float)
    PUMercado = db.Column(db.Float)
    ValorMercado = db.Column(db.Float)
    PUJuros = db.Column(db.Float)
    ValorJuros = db.Column(db.Float)
    DataVolta = db.Column(db.VARCHAR, nullable=True)
    TaxaVolta = db.Column(db.Float)
    PUVolta = db.Column(db.Float)
    ValorVolta = db.Column(db.Float)
    ValorIR = db.Column(db.Float)
    ValorIOF = db.Column(db.Float)
    TipoNegociacao = db.Column(db.Integer)
    PUCorrecao = db.Column(db.Float)
    ValorCorrecao = db.Column(db.Float)
    TaxaOperacao = db.Column(db.Float)
    IdAgente = db.Column(db.Integer, nullable=True)
    IdCustodia = db.Column(db.Integer)
    CustoCustodia = db.Column(db.Float)
    IdIndiceVolta = db.Column(db.Integer, nullable=True)
    IdOperacao = db.Column(db.Float)
    OperacaoTermo = db.Column(db.String)
    ValorCurvaVencimento = db.Column(db.Float)
    PUCurvaVencimento = db.Column(db.Float)
    AjusteMTM = db.Column(db.Float)
    AjusteVencimento = db.Column(db.Float)
    TaxaMTM = db.Column(db.Float)
    IdCorretora = db.Column(db.Integer, nullable=True)
    ValorBrutoGrossUp = db.Column(db.Float)
    AliquotaIR = db.Column(db.Float)
    AliquotaIOF = db.Column(db.Float)
    PrazoDecorridoDC = db.Column(db.Integer)
    PrazoDecorridoDU = db.Column(db.Integer)
    PuCusto = db.Column(db.Float)
    Duration = db.Column(db.Float, nullable=True)
    FatorPreviaIndexador = db.Column(db.Float, nullable=True)
    PUMtmAntesGrossUP = db.Column(db.Float)
    PUNotional = db.Column(db.Float, nullable=True)
    PUPar = db.Column(db.Float, nullable=True)
    PULimpo = db.Column(db.Float)
    PercentualValorFace = db.Column(db.Float)
    ValorAgio = db.Column(db.Float, nullable=True)
    VersaoMotorCalculo = db.Column(db.String, nullable=True)
    IdPosicaoExterna = db.Column(db.Integer, nullable=True)


class RendaFixaPos(RendaFixaBase):
    __tablename__ = "rendafixa_pos"
    DataHistorico = db.Column(db.Date)
    DataVencimento = db.Column(db.Date)
    DataOperacao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    DataVolta = db.Column(db.Date, nullable=True)


class StageRendaFixaPos(RendaFixaBase):
    __tablename__ = "stage_" + RendaFixaPos.__tablename__

    DataVolta = db.Column(db.VARCHAR, nullable=True, default=null())
    IdAgente = db.Column(db.Integer, nullable=True, default=null())
    IdIndiceVolta = db.Column(db.Integer, nullable=True, default=null())
    IdCorretora = db.Column(db.Integer, nullable=True, default=null())
    Duration = db.Column(db.Float, nullable=True, default=null())
    FatorPreviaIndexador = db.Column(db.Float, nullable=True, default=null())
    PUNotional = db.Column(db.Float, nullable=True, default=null())
    PUPar = db.Column(db.Float, nullable=True, default=null())
    ValorAgio = db.Column(db.Float, nullable=True, default=null())
    VersaoMotorCalculo = db.Column(db.String, nullable=True, default=null())
    IdPosicaoExterna = db.Column(db.Integer, nullable=True, default=null())
    
