from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship


class DistribuidorEntry(Base):
    __tablename__ = "distribuidor_entry"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    Cpfcnpj = db.Column(db.String(50))
    name = db.Column(db.String)

    rates = relationship("DistribuidorRates")
    quotaholder = relationship("DistribuidorQuotaholder")


class DistribuidorQuotaholder(Base):
    __tablename__ = "distribuidor_quotaholder"

    IdDistribuidor = db.Column(db.Integer, db.ForeignKey("distribuidor_entry.id"))
    IdCotista = db.Column(db.Integer, autoincrement=True, primary_key=True)
    CpfcnpjCotista = db.Column(db.String(50))
    NomeCotista = db.Column(db.String)

    operations = relationship("CotistaOP")


class DistribuidorRates(Base):
    __tablename__ = "distribuidor_rates"

    IdDistribuidor = db.Column(
        db.Integer, db.ForeignKey("distribuidor_entry.id"), primary_key=True
    )

    rate = db.Column(db.Float)
    initial_date = db.Column(db.Date, primary_key=True)
    end_date = db.Column(db.Date)


class CotistaOpBase(Base):
    __abstract__ = True

    IdOperacao = db.Column(db.Integer, primary_key=True, autoincrement=False)
    IdCotista = db.Column(db.Integer)
    NomeCotista = db.Column(db.String)
    CodigoInterface = db.Column(db.String)
    IdCarteira = db.Column(db.Integer)
    NomeFundo = db.Column(db.String)
    DataOperacao = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    DataAgendamento = db.Column(db.Date)
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
    CpfcnpjCotista = db.Column(db.String)
    Fonte = db.Column(db.Integer)
    IdConta = db.Column(db.Integer, nullable=True)
    IdContaCotista = db.Column(db.Integer)
    CotaInformada = db.Column(db.Float, nullable=True)
    IdAgenda = db.Column(db.Integer, nullable=True)
    IdOperacaoResgatada = db.Column(db.Integer, nullable=True)
    CodigoAnbima = db.Column(db.String)
    MovimentoCarteira = db.Column(db.String, nullable=True)
    SituacaoOperacao = db.Column(db.Integer)


class CotistaOp(CotistaOpBase):
    __tablename__ = "cotista_op"

    IdCotista = db.Column(
        db.Integer, db.ForeignKey("distribuidor_quotaholder.IdCotista")
    )


class TempCotistaOp(CotistaOpBase):
    __tablename__ = "temp_" + CotistaOp.__tablename__
