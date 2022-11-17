from api.app import db


def Column(*args, **kwargs) -> db.Column:
    """
    Creates a wrapper for the columns.
    With the default arguments being Nullable=False.
    Instead of the Nullable=True in sqlalchemy.

    Returns
    -------
    db.Column
    """
    kwargs.setdefault("nullable", False)
    return db.Column(*args, **kwargs)


class SectorEntry(db.Model):
    __tablename__ = "sector_entry"
    id = Column(db.Integer, autoincrement=True,  primary_key=True)
    methodology = Column(db.String(50))
    sector = Column(db.String(50),nullable=True)
    subsector = Column(db.String(50),nullable=True)

    assets = db.relationship("AssetsSector", lazy=True)


class AssetsSector(db.Model):
    __tablename__ = "asset_sector"

    ticker = Column(db.String(50), primary_key=True)
    sector_entry_id = Column(db.Integer, db.ForeignKey("sector_entry.id"), primary_key =True) 
    

    


# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
#https://medium.com/craftsmenltd/flask-with-sqlalchemy-marshmallow-2ec34ecfd9d4