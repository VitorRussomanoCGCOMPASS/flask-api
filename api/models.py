from api.app import db


class VNA(db.Model):
    """
    Attributes
    ----------
    __tablename__ = "vna_anbima"
    Primary keys
    -----------
    data_referencia : Column(db.Date)
    codigo_selic: Column(db.Integer)
    Others
    ------
    tipo_titulo: Column(db.String)
    index: Column(db.Float)
    tipo_correcao: Column(db.String)
    data_validade: Column(db.Date)
    vna: Column(db.Float)
    Relationships
    --------------
    None
    Methods
    -------
    """

    __tablename__ = "anbima_vna"

    data_referencia = db.Column(db.Date, primary_key=True)
    tipo_titulo = db.Column(db.String(50))
    codigo_selic = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Float)
    tipo_correcao = db.Column(db.String)
    data_validade = db.Column(db.Date)
    vna = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"{self.codigo_selic} at {self.data_referencia}"