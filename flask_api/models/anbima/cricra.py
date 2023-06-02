import sqlalchemy as db

from flask_api.models.base_model import Base

class CriCraBase(Base):

    __abstract__ = True
    codigo_ativo = db.Column(db.String(50), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)

    emissor = db.Column(db.VARCHAR(255))
    originador = db.Column(db.VARCHAR(255))
    originador_credito = db.Column(db.VARCHAR(255))
    serie = db.Column(db.NVARCHAR)
    emissao = db.Column(db.NVARCHAR)
    tipo_contrato = db.Column(db.String)
    data_vencimento = db.Column(db.Date)
    tipo_remuneracao = db.Column(db.String)
    taxa_correcao = db.Column(db.Float)
    data_finalizado = db.Column(db.String)
    
    taxa_compra = db.Column(db.Float, nullable=True)
    taxa_venda = db.Column(db.Float, nullable=True)
    taxa_indicativa = db.Column(db.Float, nullable=True)
    desvio_padrao = db.Column(db.Float, nullable=True)
    vl_pu = db.Column(db.Float, nullable=True)
    pu = db.Column(db.Float, nullable=True)
    percent_pu_par = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Float, nullable=True)
    percent_reune = db.Column(db.Float, nullable=True)
    data_referencia_ntnb = db.Column(db.Date, nullable=True)
    referencia_ntnb = db.Column(db.Date, nullable=True)
    status_t3 = db.Column(db.VARCHAR)



class CriCra(CriCraBase):
    """
    Attributes
    ----------
    __tablename__ = "cricra_anbima"

    Primary keys
    -----------
    data_referencia : db.Column(db.Date)
        Reference date of the information provided
    codigo_ativo: db.Column(db.String)
        Asset code for the bond
    Others
    ------
    emissor:db.Column(db.String)
        Securitization company responsible for issuing the paper
    originador: db.Column(db.String)
    originador_credito:db.Column(db.String)
        Company that granted the credit for the
        real estate project or for the rural production
    serie:db.Column(db.Integer)
    emissao:db.Column(db.Integer)
        Issue number
    data_vencimento:db.Column(db.Date)
        Maturity date
    taxa_compra:db.Column(db.Float)
        Average Buy rate
    taxa_venda:db.Column(db.Float)
        Average Sell rate
    taxa_indicativa:db.Column(db.Float)
        Indicative rate calculated by Anbima and used as reference price
    desvio_padrao:db.Column(db.Float)
        Sample standard deviation
    vl_pu: db.Column(db.Float)
    pu:db.Column(db.Float)
        Unit price
    percent_pu_par:db.Column(db.Float)
        Par value
    duration:db.Column(db.Float)
        Average term in which the holder will recover the investment made when acquiring the paper
    tipo_remuneracao:db.Column(db.String)
        Informs the type of return
    taxa_correcao:db.Column(db.Float)
        Issuance rate
    tipo_contrato: db.Column(db.String)

    percent_reune:db.Column(db.Float)
        Percentage of business contribution in the indicative rate
    data_referencia_ntnb:db.Column(db.Date)

    referencia_ntnb:db.Column(db.Date)
        Marutiry of the bond when remuneration is based on IPCA
    Relationships
    --------------
    None



    """

    __tablename__ = "anbima_cricra"
    serie = db.Column(db.Integer)


class StageCriCra(CriCraBase):
    __tablename__ = "stage_" + CriCra.__tablename__

