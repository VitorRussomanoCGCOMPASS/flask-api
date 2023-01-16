from api.models.sector import SectorEntry, AssetsSector
from api.schemas.base_schema import CustomSchema
from marshmallow import fields,RAISE


from app import database



class SectorEntrySchema(CustomSchema):
    class Meta:
        model = SectorEntry
        unknown =RAISE
        load_instance= True
        sqla_session = database.session

class AssetsSectorSchema(CustomSchema):
    class Meta:
        model = AssetsSector
        unknwon =RAISE
        load_instance=True
        load_relationships =True
    
        
    sector_entry = fields.Nested(SectorEntrySchema)
