from flask_api.models.base_model import Base, Column
import sqlalchemy as db


class Debentures(Base):
    """
    Attributes
    ----------
    __tablename__ = "debentures"

    Primary keys
    -----------
    data_referencia : Column(db.Date)
        Reference date (dd-mm-yyyy)

    codigo_ativo: Column(db.String)
        Debenture code (CETIP code)

    Others
    ------
    pu :Column(db.Float, nullable=True)
        Unit price
    grupo : Column(db.String)
        Index type
    duration : Column(db.Integer)
        Duration (business days) (no decimal place)
    taxa_indicativa : Column(db.Float)
        Indicative Rate
    percentual_taxa : Column(db.String)
        Issuance Rate (%)

    Relationships
    --------------
    None


    Methods
    -------

    """

    __tablename__ = "debentures"
    codigo_ativo = Column(db.String(30), primary_key=True)
    data_referencia = Column(db.Date, primary_key=True)

    pu = Column(db.Float, nullable=True)
    grupo = Column(db.String)
    duration = Column(db.Integer, nullable=True)
    taxa_indicativa = Column(db.Float)
    percentual_taxa = Column(db.String)
    precification_method = Column(db.String)


class AnbimaDebentures(Debentures):
    """
    Polymorphic identity of debentures that refers
    only to the anbima debentures

    Attributes
    ----------
    __tablename__ = "debentures"

    Primary keys
    -----------
    data_referencia : Column(db.Date)
        Reference date (dd-mm-yyyy)

    codigo_ativo: Column(db.String)
        Debenture code (CETIP code)

    Others
    ------

    pu :Column(db.Float, nullable=True)
        Unit price
    grupo : Column(db.String)
        Index type
    duration : Column(db.Integer)
        Duration (business days) (no decimal place)
    taxa_indicativa : Column(db.Float)
        Indicative Rate
    percentual_taxa : Column(db.String)
        Issuance Rate (%)

    Polymorphic specific
    -----------
    data_vencimento:Column(db.Date)
        Maturity date (dd-mm-yyyy)
    taxa_compra:Column(db.Float, nullable=True)
        Buy rate
    taxa_venda:Column(db.Float, nullable=True)
        Sell rate
    desvio_padrao:Column(db.Float)
        Sample standard deviation
    val_min_intervalo:Column(db.Float)
        Lower indicative range
    val_max_intervalo:Column(db.Float)
        Upper indicative range
    percent_pu_par:Column(db.Float)
        Par value
    percent_reune:Column(db.Float, nullable=True)
        %of business contribution in the indicative rate
    emissor:Column(db.String)
        Issuer name
    referencia_ntnb:Column(db.Date, nullable=True)
        NTN-B reference (dd-mm-yyyy)
    data_finalizado: Column(db.Date)

    Relationships
    --------------
    None


    Methods
    -------

    """

    __mapper_args__ = {
        "polymorphic_identity": "anbima",
        "polymorphic_on": "precification_method",
    }

    data_vencimento = Column(db.Date)
    data_finalizado = Column(db.Date)
    taxa_compra = Column(db.Float, nullable=True)
    taxa_venda = Column(db.Float, nullable=True)
    desvio_padrao = Column(db.Float)
    val_min_intervalo = Column(db.Float)
    val_max_intervalo = Column(db.Float)
    percent_pu_par = Column(db.Float, nullable=True)
    percent_reune = Column(db.Float, nullable=True)
    emissor = Column(db.String)
    referencia_ntnb = Column(db.Date, nullable=True)


class OtherDebentures(Debentures):

    __mapper_args__ = {
        "polymorphic_identity": "non-anbima",
        "polymorphic_on": "precification_method",
    }
