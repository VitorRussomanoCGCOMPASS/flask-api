from api.models.base_model import Base, Column
import sqlalchemy as db


class MarketIndex(Base):
    __tablename__ = "market_index"

    index = Column(db.String(50), primary_key=True)
    segment = Column(db.String(50), nullable=True)
    date = Column(db.Date, primary_key=True)
    cod = Column(db.String(50), primary_key=True)
    asset = Column(db.String(50))
    type = Column(db.String(50))

    part = Column(db.Float)
    partAcum = Column(db.Float, nullable=True)
    theoricalQty = Column(db.Float)
