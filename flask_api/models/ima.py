import sqlalchemy as db
from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from flask_api.models.base_model import Base, Column


class IMA(Base):
    """
    Attributes
    ----------
    __tablename__ = "ima_anbima"

    Primary Keys
    -----------
    indice: Column(db.String)
        Index name
    data_referencia: Column(db.Date)
        Referential date (yyyy-mm-ddd)
    Others
    ------
    variacao_ult12m : Column(db.Float)
        (%) Variation of the last 12 months
    variacao_ult24m : Column(db.Float)
        (%) Variation of the last 24 months
    numero_indice : Column(db.Float)
        Index number
    variacao_diaria : Column(db.Float)
        (%) Daily variation
    variacao_anual : Column(db.Float)
        (%) Annual variation
    variacao_mensal : Column(db.Float)
        (%) Monthly variation
    peso_indice : Column(db.Float, nullable=True)
        Weight in IMA-General
    quantidade_titulos : Column(db.Float)
        Quantity of bonds in the index
    valor_mercado : Column(db.Float)
        Portfolio at market value
    pmr : Column(db.Float)
        Average term for renegotiation of index portfolio on consecutive days
    convexidade : Column(db.Float, nullable=True)
        Convexity
    duration : Column(db.Float)
        Index duration
    yield_col : Column("yield", db.Float, nullable=True)
        Yield
    redemption_yield : Column(db.Float, nullable=True)
        Redemption yield

    Relationships
    ------------
    components:  One to many with components_ima_anbima

    Methods
    -------
    find_all()

    find_by_id()

    """

    __tablename__ = "ima_anbima"
    
    indice = Column(db.String(30))
    data_referencia = Column(db.Date)
    variacao_ult12m = Column(db.Float)
    variacao_ult24m = Column(db.Float)
    numero_indice = Column(db.Float)
    variacao_diaria = Column(db.Float)
    variacao_anual = Column(db.Float)
    variacao_mensal = Column(db.Float)
    peso_indice = Column(db.Float, nullable=True)
    quantidade_titulos = Column(db.Float)
    valor_mercado = Column(db.Float)
    pmr = Column(db.Float)
    convexidade = Column(db.Float, nullable=True)
    duration = Column(db.Float)
    yield_col = Column("yield", db.Float, nullable=True)
    redemption_yield = Column(db.Float, nullable=True)

    components = relationship("ComponentsIMA", backref="ima_anbima")
    __table_args__ = (PrimaryKeyConstraint(indice, data_referencia), {})

    def __repr__(self) -> str:
        return f"{self.indice} at {self.data_referencia}"



class ComponentsIMA(Base):
    """

    Attributes
    ----------
    __tablename__ = "components_ima_anbima"

    Primary Key
    -----------
    indice: Column(db.String)
        Index name
    data_referencia: Column(db.Date)
        Referential date (dd-mm-yyyy)
    tipo_titulo:Column(db.String)
        Bond type
    data_vencimento : Column(db.Date)
        Maturity date (dd-mm-yyyy)

    Others
    -----
    codigo_selic : Column(db.Integer)
        Selic code
    codigo_isin : Column(db.String)
        Isin code
    taxa_indicativa : Column(db.Float)
        Indicative Rate
    pu : Column(db.Float)
        Unitary price (BRL)
    pu_juros : Column(db.Float)
        Bond interest unit price
    quantidade_componentes : Column(db.Float)
        Component quantity
    quantidade_teorica : Column(db.Float)
        Theorical amount of component in the index
    valor_mercado : Column(db.Float)
         Portfolio at market value
     peso_componente : Column(db.Float)
        Weight in IMA-General
    prazo_vencimento : Column(db.Float)
        Maturity date of bond (dd-mm-yyyy)
    duration : Column(db.Float)
        Index duration
    pmr : Column(db.Float)
        Average term for renegotiation of indxe portfolio on consecutive days
    convexidade : Column(db.Float)
        Convexity

    Methods
    -------
    find_by_type(date: datetime.date, expiration: datetime.date,debenture_type: str, session: Session)
    """

    __tablename__ = "components_ima_anbima"
    indice = Column(db.String(30), primary_key=True)
    data_referencia = Column(db.Date, primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            [indice, data_referencia], [IMA.indice, IMA.data_referencia]
        ),
        {},
    )

    tipo_titulo = Column(db.String(30), primary_key=True)
    data_vencimento = Column(db.Date, primary_key=True)
    codigo_selic = Column(db.Integer)
    codigo_isin = Column(db.String)
    taxa_indicativa = Column(db.Float)
    pu = Column(db.Float)
    pu_juros = Column(db.Float)
    quantidade_componentes = Column(db.Float)
    quantidade_teorica = Column(db.Float)
    valor_mercado = Column(db.Float)
    peso_componente = Column(db.Float)
    prazo_vencimento = Column(db.Float)
    duration = Column(db.Float)
    pmr = Column(db.Float)
    convexidade = Column(db.Float)

    def __repr__(self) -> str:
        return f"{self.codigo_isin} named {self.tipo_titulo} expiring at {self.data_vencimento}"


