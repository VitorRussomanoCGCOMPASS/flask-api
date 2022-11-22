from api.models.base_model import Base, Column
import sqlalchemy as db
from sqlalchemy.orm import relationship

class SectorEntry(Base):
    __tablename__ = "sector_entry"
    id = Column(db.Float, autoincrement=True, primary_key=True)
    methodology = Column(db.String(50))
    sector = Column(db.String(50),nullable=True)
    subsector = Column(db.String(50),nullable=True)

    # assets = relationship("AssetsSector", backref="sector_entry", lazy=True)
