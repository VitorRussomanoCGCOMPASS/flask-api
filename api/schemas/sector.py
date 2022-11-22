from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import RAISE
from api.models.sector import SectorEntry

class SectorEntrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SectorEntry 
        unknown = RAISE

