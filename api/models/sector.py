from api.models.base_model import Base, Column
import sqlalchemy as db
from sqlalchemy.orm import relationship


class SectorEntry(Base):
    __tablename__ = "sector_entry"
    id = Column(db.Integer, primary_key=True)
    methodology = Column(db.String(50))
    sector = Column(db.String(50), nullable=True)
    subsector = Column(db.String(50), nullable=True)

    assets = relationship("AssetsSector", back_populates="sector_entry", lazy=True)


class AssetsSector(Base):
    __tablename__ = "assets_sector"

    ticker = Column(db.String(50), primary_key=True)
    sector_entry = relationship("SectorEntry", back_populates="assets")
    sector_id = Column(db.Integer, db.ForeignKey("sector_entry.id"), primary_key=True)
