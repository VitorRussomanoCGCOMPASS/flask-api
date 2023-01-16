import sqlalchemy as db
from sqlalchemy.orm import relationship

from flask_api.models.base_model import Base, Column


class Indexes(Base):

    __tablename__ = "indexes"

    id = Column(db.Integer, autoincrement=True, primary_key=True)
    index = Column(db.String(50))
    values = relationship("IndexValues", back_populates="index")


class IndexValues(Base):
    __tablename__ = "indexes_values"
    date = Column(db.Date, primary_key=True)
    index = relationship("Indexes", back_populates="values")
    index_id = Column(db.Integer, db.ForeignKey("indexes.id"), primary_key=True)
    value = Column(db.Float)
