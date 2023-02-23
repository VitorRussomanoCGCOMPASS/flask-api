from flask_api.models.base_model import Base
import sqlalchemy as db
from sqlalchemy.orm import relationship

""" 
class CotistaOp_old(Base):

    __tablename__ = "cotista_op_old"

    IdOperacao = db.Column(db.Integer, primary_key=True,autoincrement=False)
    IdCotista = db.Column(db.Integer)
    ApelidoCotista = db.Column(db.String)
    IdCarteira = db.Column(db.Integer)
    ApelidoCarteira = db.Column(db.String)
    CnpjCarteira = db.Column(db.String)
    ApelidoDistribuidor = db.Column(db.String, nullable=True)
    CnpjDistribuidor = db.Column(db.String, nullable=True)
    ApelidoGestor = db.Column(db.String, nullable=True)
    CnpjGestor = db.Column(db.String, nullable=True)
    ApelidoAdministrador = db.Column(db.String, nullable=True)
    CnpjAdministrador = db.Column(db.String, nullable=True)
    Serie = db.Column(db.Integer, nullable=True)
    DataOperacao = db.Column(db.Date)
    DataRegistro = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    TipoOperacao = db.Column(db.Integer)
    DescricaoTipoOperacao = db.Column(db.String)
    ValorBruto = db.Column(db.Float)
    ValorIr = db.Column(db.Float)
    ValorIof = db.Column(db.Float)
    ValorLiquido = db.Column(db.Float)
    Quantidade = db.Column(db.Float)
    TipoLiquidacao = db.Column(db.String)
    IdPosicaoResgatada = db.Column(db.Integer, nullable=True)
    DataAplicCautelaResgatada = db.Column(db.Date, nullable=True)
    ContaFundo = db.Column(db.String)
    ContaDistribuidor = db.Column(db.String, nullable=True) """


class DistribuidorEntry(Base):
    __tablename__ =  'distribuidor_entry'

    Cpfcnpj = db.Column(db.String(50),primary_key=True)
    name = db.Column(db.String)

    rates = relationship('DistribuidorRates')
    quotaholder = relationship('DistribuidorQuotaholder')



class DistribuidorQuotaholder(Base):
    __tablename__ = 'distribuidor_quotaholder'

    IdCotista = db.Column(db.Integer,autoincrement=True,primary_key=True)
    CpfcnpjCotista = db.Column(db.String(50))
    NomeCotista = db.Column(db.String)
    
    CpfcnpjDistribuidor = db.Column(db.String, db.ForeignKey("distribuidor_entry.Cpfcnpj"))
    NomeDistribuidor = db.Column(db.String, db.ForeignKey("distribuidor_entry.name"))

    operations = relationship('CotistaOP')


class DistribuidorRates(Base):
    __tablename__ = 'distribuidor_rates'

    cpfcnpjDistribuidor = db.Column(db.String, db.ForeignKey('distribuidor_entry.Cpfcnpj'),primary_key=True)
    
    rate = db.Column(db.Float)
    initial_date = db.Column(db.Date,primary_key=True)
    end_date = db.Column(db.Date)


class CotistaOP(Base):
    __tablename__ = 'cotista_op'


    IdOperacao = db.Column(db.Integer, primary_key=True,autoincrement=False)
    IdCotista = db.Column(db.Integer)
    NomeCotista = db.Column(db.String)
    CodigoInterface=  db.Column(db.String)
    IdCarteira = db.Column(db.Integer)
    NomeFundo = db.Column(db.String)
    DataOperacao = db.Column(db.Date)
    DataConversao = db.Column(db.Date)
    DataLiquidacao = db.Column(db.Date)
    DataAgendamento = db.Column(db.Date)
    TipoOperacao  =db.Column(db.Integer)
    TipoResgate =db.Column(db.Integer,nullable=True)
    IdPosicaoResgatada = db.Column(db.Integer,nullable=True)
    IdFormaLiquidacao = db.Column(db.Integer)
    Quantidade =db.Column(db.Float)
    CotaOperacao = db.Column(db.Float)
    ValorBruto = db.Column(db.Float)
    ValorLiquido = db.Column(db.Float)
    ValorIR = db.Column(db.Float)
    ValorIOF = db.Column(db.Float)
    ValorCPMF = db.Column(db.Float)
    ValorPerfomance = db.Column(db.Float)
    PrejuizoUsado = db.Column(db.Float)
    RendimentoResgate = db.Column(db.Float)
    VariacaoResgate=  db.Column(db.Float)
    Observacao = db.Column(db.String,nullable=True)
    DadosBancarios = db.Column(db.String,nullable=True)
    CpfcnpjCarteira = db.Column(db.String)
    CpfcnpjCotista = db.Column(db.String)
    Fonte = db.Column(db.Integer)
    IdConta = db.Column(db.Integer,nullable=True)
    IdContaCotista = db.Column(db.Integer)
    CotaInformada =db.Column(db.Float,nullable=True)
    IdAgenda = db.Column(db.Integer,nullable=True)
    IdOperacaoResgatada =db.Column(db.Integer,nullable=True)
    CodigoAnbima = db.Column(db.String)
    MovimentoCarteira = db.Column(db.String,nullable=True)
    SituacaoOperacao = db.Column(db.Integer)