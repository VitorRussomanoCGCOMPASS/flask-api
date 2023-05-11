import sqlalchemy as db
from sqlalchemy import ForeignKeyConstraint, func, null, select
from sqlalchemy.orm import relationship

from flask_api.models.base_model import Base
from flask_api.models.views import View


class StageIMA(Base):
    __tablename__ = "stage_anbima_ima"

    indice = db.Column(db.String(30), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)
    variacao_ult12m = db.Column(db.Float)
    variacao_ult24m = db.Column(db.Float)
    numero_indice = db.Column(db.Float)
    variacao_diaria = db.Column(db.Float)
    variacao_anual = db.Column(db.Float)
    variacao_mensal = db.Column(db.Float)
    peso_indice = db.Column(db.Float, nullable=True, default=null())
    quantidade_titulos = db.Column(db.Float)
    valor_mercado = db.Column(db.Float)
    pmr = db.Column(db.Float)
    convexidade = db.Column(db.Float, nullable=True, default=null())
    duration = db.Column(db.Float)
    yield_col = db.Column("yield", db.Float, nullable=True, default=null())
    redemption_yield = db.Column(db.Float, nullable=True, default=null())
    componentes = db.Column(db.JSON)


class IMABase(Base):
    __abstract__ = True

    indice = db.Column(db.String(30), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)
    variacao_ult12m = db.Column(db.Float)
    variacao_ult24m = db.Column(db.Float)
    numero_indice = db.Column(db.Float)
    variacao_diaria = db.Column(db.Float)
    variacao_anual = db.Column(db.Float)
    variacao_mensal = db.Column(db.Float)
    peso_indice = db.Column(db.Float, nullable=True)
    quantidade_titulos = db.Column(db.Float)
    valor_mercado = db.Column(db.Float)
    pmr = db.Column(db.Float)
    convexidade = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Float)
    _yield = db.Column("yield", db.Float, nullable=True)
    redemption_yield = db.Column(db.Float, nullable=True)


class IMA(IMABase):
    """
    Attributes
    ----------
    __tablename__ = "ima_anbima"

    Primary Keys
    -----------
    indice: db.Column(db.String)
        Index name
    data_referencia: db.Column(db.Date)
        Referential date (yyyy-mm-ddd)
    Others
    ------
    variacao_ult12m : db.Column(db.Float)
        (%) Variation of the last 12 months
    variacao_ult24m : db.Column(db.Float)
        (%) Variation of the last 24 months
    numero_indice : db.Column(db.Float)
        Index number
    variacao_diaria : db.Column(db.Float)
        (%) Daily variation
    variacao_anual : db.Column(db.Float)
        (%) Annual variation
    variacao_mensal : db.Column(db.Float)
        (%) Monthly variation
    peso_indice : db.Column(db.Float, nullable=True)
        Weight in IMA-General
    quantidade_titulos : db.Column(db.Float)
        Quantity of bonds in the index
    valor_mercado : db.Column(db.Float)
        Portfolio at market value
    pmr : db.Column(db.Float)
        Average term for renegotiation of index portfolio on consecutive days
    convexidade : db.Column(db.Float, nullable=True)
        Convexity
    duration : db.Column(db.Float)
        Index duration
    yield_col : db.Column("yield", db.Float, nullable=True)
        Yield
    redemption_yield : db.Column(db.Float, nullable=True)
        Redemption yield

    Relationships
    ------------
    components:  One to many with components_ima_anbima


    """

    __tablename__ = "anbima_ima"

    components = relationship("ComponentsIMA", backref="anbima_ima")




class ComponentsIMA(Base):
    """

    Attributes
    ----------
    __tablename__ = "components_ima_anbima"

    Primary Key
    -----------
    indice: db.Column(db.String)
        Index name
    data_referencia: db.Column(db.Date)
        Referential date (dd-mm-yyyy)
    tipo_titulo:db.Column(db.String)
        Bond type
    data_vencimento : db.Column(db.Date)
        Maturity date (dd-mm-yyyy)

    Others
    -----
    codigo_selic : db.Column(db.Integer)
        Selic code
    codigo_isin : db.Column(db.String)
        Isin code
    taxa_indicativa : db.Column(db.Float)
        Indicative Rate
    pu : db.Column(db.Float)
        Unitary price (BRL)
    pu_juros : db.Column(db.Float)
        Bond interest unit price
    quantidade_componentes : db.Column(db.Float)
        Component quantity
    quantidade_teorica : db.Column(db.Float)
        Theorical amount of component in the index
    valor_mercado : db.Column(db.Float)
         Portfolio at market value
     peso_componente : db.Column(db.Float)
        Weight in IMA-General
    prazo_vencimento : db.Column(db.Float)
        Maturity date of bond (dd-mm-yyyy)
    duration : db.Column(db.Float)
        Index duration
    pmr : db.Column(db.Float)
        Average term for renegotiation of indxe portfolio on consecutive days
    convexidade : db.Column(db.Float)
        Convexity

    Methods
    -------
    find_by_type(date: datetime.date, expiration: datetime.date,debenture_type: str, session: Session)
    """

    __tablename__ = "anbima_ima_components"

    indice = db.Column(db.String(30), primary_key=True)
    data_referencia = db.Column(db.Date, primary_key=True)


    tipo_titulo = db.Column(db.String(30), primary_key=True)
    data_vencimento = db.Column(db.Date, primary_key=True)
    codigo_selic = db.Column(db.Integer)
    codigo_isin = db.Column(db.String)
    taxa_indicativa = db.Column(db.Float)
    pu = db.Column(db.Float)
    pu_juros = db.Column(db.Float)
    quantidade_componentes = db.Column(db.Float)
    quantidade_teorica = db.Column(db.Float)
    valor_mercado = db.Column(db.Float)
    peso_componente = db.Column(db.Float)
    prazo_vencimento = db.Column(db.Float)
    duration = db.Column(db.Float)
    pmr = db.Column(db.Float)
    convexidade = db.Column(db.Float)


    __table_args__ = (
        ForeignKeyConstraint(
            [indice, data_referencia], [IMA.indice, IMA.data_referencia]
        ),
        {},
    )


class StageComponentsIMAView(Base):
    __table__ = View(
        "stage_anbima_componentsIMA",
        Base.metadata,
        select(
            StageIMA.data_referencia,
            StageIMA.indice,
            func.JSON_VALUE(StageIMA.componentes, "$[0].tipo_titulo").label(
                "tipo_titulo"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].data_vencimento").label(
                "data_vencimento"
            ),
            
            func.JSON_VALUE(StageIMA.componentes, "$[0].codigo_selic").label(
                "codigo_selic"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].codigo_isin").label(
                "codigo_isin"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].taxa_indicativa").label(
                "taxa_indicativa"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].pu").label("pu"),
            func.JSON_VALUE(StageIMA.componentes, "$[0].pu_juros").label("pu_juros"),
            func.JSON_VALUE(
                StageIMA.componentes, "$[0].quantidade_componentes"
            ).label("quantidade_componentes"),
            func.JSON_VALUE(StageIMA.componentes, "$[0].quantidade_teorica").label(
                "quantidade_teorica"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].valor_mercado").label(
                "valor_mercado"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].peso_componente").label(
                "peso_componente"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].prazo_vencimento").label(
                "prazo_vencimento"
            ),
            func.JSON_VALUE(StageIMA.componentes, "$[0].duration").label("duration"),
            func.JSON_VALUE(StageIMA.componentes, "$[0].pmr").label("pmr"),
            func.JSON_VALUE(StageIMA.componentes, "$[0].convexidade").label(
                "convexidade"
            ),
        ),
    )



