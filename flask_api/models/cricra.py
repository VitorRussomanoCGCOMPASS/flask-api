from flask_api.models.base_model import Base,Column
import sqlalchemy as db



class CriCra(Base):
    """
    Attributes
    ----------
    __tablename__ = "cricra_anbima"

    Primary keys
    -----------
    data_referencia : Column(db.Date)
        Reference date of the information provided
    codigo_ativo: Column(db.String)
        Asset code for the bond
    Others
    ------
    emissor:Column(db.String)
        Securitization company responsible for issuing the paper
    originador: Column(db.String)
    originador_credito:Column(db.String)
        Company that granted the credit for the
        real estate project or for the rural production
    serie:Column(db.Integer)
    emissao:Column(db.Integer)
        Issue number
    data_vencimento:Column(db.Date)
        Maturity date
    taxa_compra:Column(db.Float)
        Average Buy rate
    taxa_venda:Column(db.Float)
        Average Sell rate
    taxa_indicativa:Column(db.Float)
        Indicative rate calculated by Anbima and used as reference price
    desvio_padrao:Column(db.Float)
        Sample standard deviation
    vl_pu: Column(db.Float)
    pu:Column(db.Float)
        Unit price
    percent_pu_par:Column(db.Float)
        Par value
    duration:Column(db.Float)
        Average term in which the holder will recover the investment made when acquiring the paper
    tipo_remuneracao:Column(db.String)
        Informs the type of return
    taxa_correcao:Column(db.Float)
        Issuance rate
    tipo_contrato: Column(db.String)

    percent_reune:Column(db.Float)
        Percentage of business contribution in the indicative rate
    data_referencia_ntnb:Column(db.Date)

    referencia_ntnb:Column(db.Date)
        Marutiry of the bond when remuneration is based on IPCA
    Relationships
    --------------
    None

    Methods
    -------
    find_by_date()


    """

    __tablename__ = "cricra_anbima"

    codigo_ativo = Column(db.String(30), primary_key=True)
    data_referencia = Column(db.Date, primary_key=True)
    emissor = Column(db.String)
    originador = Column(db.String)
    originador_credito = Column(db.String)
    serie = Column(db.Integer)
    emissao = Column(db.Integer)
    data_vencimento = Column(db.Date)
    taxa_compra = Column(db.Float, nullable=True)
    taxa_venda = Column(db.Float, nullable=True)
    taxa_indicativa = Column(db.Float, nullable=True)
    desvio_padrao = Column(db.Float, nullable=True)
    vl_pu = Column(db.Float, nullable=True)
    pu = Column(db.Float, nullable=True)
    percent_pu_par = Column(db.Float, nullable=True)
    duration = Column(db.Float, nullable=True)
    tipo_remuneracao = Column(db.String)
    taxa_correcao = Column(db.Float)
    data_finalizado = Column(db.Date)  # Type: '2022-10-06T19:18:55.213514' #cade
    percent_reune = Column(db.Float, nullable=True)
    data_referencia_ntnb = Column(db.Date, nullable=True)
    referencia_ntnb = Column(db.Date, nullable=True)
    tipo_contrato = Column(db.String, nullable=True)

