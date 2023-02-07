from flask_api.models.base_model import Base, Column
import sqlalchemy as db


class DevOps(Base):
    __tablename__ = "devops"

    id = Column(db.Integer, autoincrement=False, primary_key=True)
    name = Column((db.String))
    dag = Column(db.String(50), primary_key=True)
    task_group = Column(db.String(50), primary_key=True, nullable=True)
