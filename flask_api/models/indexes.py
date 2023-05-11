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
    __tablename__ = "stage_" + IndexValues.__tablename__
    Cotacoes = Column(db.JSON)
    IdIndice = Column(db.Integer, autoincrement=False, primary_key=True)
    Descricao = Column(db.String(50))


from flask_api.models.views import View
from sqlalchemy import select, func

class StageIndexView(Base):

    __table__ = View(
        "stage_indexes_values",
        Base.metadata,
        select(
            func.JSON_VALUE(StageIndexValues.Cotacoes, "$[0].Data").label(
                "date"
            ),
            func.JSON_VALUE(StageIndexValues.Cotacoes, "$[0].Valor").label(
                "value"
            ),
            StageIndexValues.IdIndice.label('index_id'),
        ),
    )
