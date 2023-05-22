from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy import null

# FIXME : DISTRIBUIDOR RATE RELATIONSHIP.
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
    positions = relationship("FundsPos")
    # distribution_rate = relationship("distribuidor_rates")


class FundsValuesBase(Base):
    __abstract__ = True

    IdCarteira = db.Column(db.Integer, primary_key=True, autoincrement=False)
    CotaAbertura = db.Column(db.Float)
    CotaFechamento = db.Column(db.Float)
    CotaBruta = db.Column(db.Float)
    PLAbertura = db.Column(db.Float)
    PLFechamento = db.Column(db.Float)
    PatrimonioBruto = db.Column(db.Float)
    QuantidadeFechamento = db.Column(db.Float)
    AjustePL = db.Column(db.Float)
    CotaImportada = db.Column(db.String)
    CotaEx = db.Column(db.Float)
    CotaRendimento = db.Column(db.Float)
    ProventoAcumulado = db.Column(db.Float)
    IdSerieOffShore = db.Column(db.Integer)


class FundsValues(FundsValuesBase):
    __tablename__ = "funds_values"
    IdCarteira = db.Column(
        db.Integer,
        db.ForeignKey("funds.britech_id"),
        primary_key=True,
        autoincrement=False,
    )

    Data = db.Column(db.Date, primary_key=True)


class StageFundsValues(FundsValuesBase):
    __tablename__ = "stage_" + FundsValues.__tablename__
    Data = db.Column(db.String(50), primary_key=True)


class BaseFundsPos(Base):

    # https://saas.britech.com.br/compass_ws/api/Fundo/BuscaPosicaoFundoPorIdCarteiraData
    __abstract__ = True

    IdPosicao = db.Column(db.Integer, primary_key=True)
    DataHistorico = db.Column(db.VARCHAR(50), primary_key=True)
    IdOperacao = db.Column(db.Integer)
    IdCliente = db.Column(db.Integer)
    IdCarteira = db.Column(db.Integer)
    ValorAplicacao = db.Column(db.Float)
    DataAplicacao = db.Column(db.VARCHAR)
    DataConversao = db.Column(db.VARCHAR)
    CotaAplicacao = db.Column(db.Float)
    CotaDia = db.Column(db.Float)
    ValorBruto = db.Column(db.Float)
    ValorLiquido = db.Column(db.Float)
    QuantidadeInicial = db.Column(db.Float)
    Quantidade = db.Column(db.Float)
    QuantidadeBloqueada = db.Column(db.Float)
    DataUltimaCobrancaIR = db.Column(db.VARCHAR)
    ValorIR = db.Column(db.Float)
    ValorIOF = db.Column(db.Float)
    ValorPerformance = db.Column(db.Float)
    ValorIOFVirtual = db.Column(db.Float)
    QuantidadeAntesCortes = db.Column(db.Float)
    ValorRendimento = db.Column(db.Float)
    DataUltimoCortePfee = db.Column(db.VARCHAR, nullable=True)
    FieTabelaIr = db.Column(db.Float, nullable=True)
    QtdePendenteLiquidacao = db.Column(db.Integer)
    ValorPendenteLiquidacao = db.Column(db.Float)
    AmortizacaoAcumuladaPorCota = db.Column(db.Float)
    JurosAcumuladoPorCota = db.Column(db.Float)
    AmortizacaoAcumuladaPorValor = db.Column(db.Float)
    JurosAcumuladoPorValor = db.Column(db.Float)
    AliquotaVigenteIOF = db.Column(db.Float)
    AliquotaVigenteIR = db.Column(db.Float)
    PerdasCompensar = db.Column(db.Float)


class FundsPos(BaseFundsPos):
    __tablename__ = "funds_pos"
    IdCarteira = db.Column(db.Integer, db.ForeignKey("funds.britech_id"))
    DataHistorico = db.Column(db.Date, primary_key=True)
    DataAplicacao = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataUltimaCobrancaIR = db.Column(db.Date)
    DataUltimoCortePfee = db.Column(db.Date, nullable=True)


class StageFundsPos(BaseFundsPos):
    __tablename__ = "stage_" + FundsPos.__tablename__

    DataUltimoCortePfee = db.Column(db.VARCHAR, nullable=True, default=null())
    FieTabelaIr = db.Column(db.Float, nullable=True, default=null())
