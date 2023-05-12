import sqlalchemy as db
from sqlalchemy.orm import relationship

from flask_api.models.base_model import Base
from flask_api.models.funds import Funds


class DistribuidorEntry(Base):
    __tablename__ = "distribuidor_entry"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    Cpfcnpj = db.Column(db.String(50))
    name = db.Column(db.String)

    admin_rate = relationship(
        "DistribuidorRates",
        primaryjoin="DistribuidorEntry.admin_rate = DistribuidorRates.admin_rate ",
    )

    perfomance_rate = relationship(
        "DistribuidorRates",
        primaryjoin="DistribuidorEntry.perfomance_rate = DistribuidorRates.perfomance_rate ",
    )

    quotaholder = relationship("DistribuidorQuotaholder")


class DistribuidorQuotaholder(Base):
    __tablename__ = "distribuidor_quotaholder"

    IdDistribuidor = db.Column(db.Integer, db.ForeignKey("distribuidor_entry.id"))

    CpfcnpjCotista = db.Column(db.String(20), primary_key=True)
    NomeCotista = db.Column(db.String)

    operations = relationship("CotistaOP")


class DistribuidorRates(Base):
    __tablename__ = "distribuidor_rates"

    IdDistribuidor = db.Column(
        db.Integer,
        db.ForeignKey("distribuidor_entry.id"),
        primary_key=True,
        autoincrement=False,
    )

    IdBritech = db.Column(db.Integer, db.ForeignKey("funds.britech_id"))

    admin_rate = db.Column(db.Float)
    perfomance_rate = db.Column(db.Float)

    initial_date = db.Column(db.Date, primary_key=True)
    end_date = db.Column(db.Date, nullable=True)


class CotistaOpBase(Base):
    __abstract__ = True

    IdOperacao = db.Column(db.Integer, primary_key=True, autoincrement=False)
    IdCotista = db.Column(db.Integer)
    NomeCotista = db.Column(db.String)
    CodigoInterface = db.Column(db.String,nullable=True)
    IdCarteira = db.Column(db.Integer)
    NomeFundo = db.Column(db.String)
    DataOperacao = db.Column(db.VARCHAR)
    DataConversao = db.Column(db.VARCHAR)
    DataLiquidacao = db.Column(db.VARCHAR)
    DataAgendamento = db.Column(db.VARCHAR)
    TipoOperacao = db.Column(db.Integer)
    TipoResgate = db.Column(db.Integer, nullable=True)
    IdPosicaoResgatada = db.Column(db.Integer, nullable=True)
    IdFormaLiquidacao = db.Column(db.Integer)
    Quantidade = db.Column(db.Float)
    CotaOperacao = db.Column(db.Float)
    ValorBruto = db.Column(db.Float)
    ValorLiquido = db.Column(db.Float)
    ValorIR = db.Column(db.Float)
    ValorIOF = db.Column(db.Float)
    ValorCPMF = db.Column(db.Float)
    ValorPerformance = db.Column(db.Float)
    PrejuizoUsado = db.Column(db.Float)
    RendimentoResgate = db.Column(db.Float)
    VariacaoResgate = db.Column(db.Float)
    Observacao = db.Column(db.String, nullable=True)
    DadosBancarios = db.Column(db.String, nullable=True)
    CpfcnpjCarteira = db.Column(db.String)
    CpfcnpjCotista = db.Column(db.String(20))
    Fonte = db.Column(db.Integer)
    IdConta = db.Column(db.Integer, nullable=True)
    IdContaCotista = db.Column(db.Integer)
    CotaInformada = db.Column(db.Float, nullable=True)
    IdAgenda = db.Column(db.Integer, nullable=True)
    IdOperacaoResgatada = db.Column(db.Integer, nullable=True)
    CodigoAnbima = db.Column(db.String)
    MovimentoCarteira = db.Column(db.String, nullable=True)
    SituacaoOperacao = db.Column(db.Integer)
    CodigoCategoriaMovimentacao = db.Column(db.String, nullable=True)
    TipoCotistaMovimentacao = db.Column(db.Integer)
    IdBoletaExterna = db.Column(db.Integer, nullable=True)
    DataDia = db.Column(db.VARCHAR)
    Status = db.Column(db.String)
    IdOperacaoAuxiliar = db.Column(db.Integer, nullable=True)
    IdCategoriaMovimentacao = db.Column(db.Integer, nullable=True)


class CotistaOp(CotistaOpBase):
    __tablename__ = "cotista_op"

    CpfcnpjCotista = db.Column(
        db.String(20),
    )
    DataOperacao = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    DataAgendamento = db.Column(db.Date)
    DataDia = db.Column(db.Date)
    # db.ForeignKey("distribuidor_quotaholder.CpfcnpjCotista")

from sqlalchemy import null


class StageCotistaOp(CotistaOpBase):
    __tablename__ = "stage_" + CotistaOp.__tablename__
    DetalheResgate = db.Column(db.JSON,nullable=True, default=null())
    CodigoInterface = db.Column(db.String,nullable=True,default=null())
    TipoResgate = db.Column(db.Integer, nullable=True,default=null())
    IdPosicaoResgatada = db.Column(db.Integer, nullable=True,default=null())
    IdConta = db.Column(db.Integer, nullable=True,default=null())
    CotaInformada = db.Column(db.Float, nullable=True,default=null())
    IdAgenda = db.Column(db.Integer, nullable=True,default=null())
    IdOperacaoResgatada = db.Column(db.Integer, nullable=True,default=null())
    CodigoCategoriaMovimentacao = db.Column(db.String, nullable=True,default=null())
    IdBoletaExterna = db.Column(db.Integer, nullable=True,default=null())
    IdOperacaoAuxiliar = db.Column(db.Integer, nullable=True,default=null())
    IdCategoriaMovimentacao = db.Column(db.Integer, nullable=True,default=null())


