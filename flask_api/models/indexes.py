import sqlalchemy as db
from sqlalchemy.orm import relationship

from flask_api.models.base_model import Base, Column


class Indexes(Base):

    __tablename__ = "indexes"

    id = Column(db.Integer, autoincrement=False, primary_key=True)
    index = Column(db.String(50))
    values = relationship("IndexValues", back_populates="index")


class IndexValues(Base):
    __tablename__ = "indexes_values"
    date = Column(db.Date, primary_key=True)
    index_id = Column(db.Integer, db.ForeignKey("indexes.id"), primary_key=True)
    value = Column(db.Float)

    index = relationship("Indexes", back_populates="values")




class StageIndexValues(Base):
    __tablename__ = 'stage_' + IndexValues.__tablename__
    Cotacoes = Column(db.JSON)
    IdIndice = Column(db.Integer, autoincrement=False, primary_key=True)
    Descricao = Column(db.String(50))

