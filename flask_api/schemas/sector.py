from flask_api.models.sector import SectorEntry, AssetsSector
from flask_api.schemas.base_schema import CustomSchema
from marshmallow import RAISE


from marshmallow_sqlalchemy.fields import Nested



class SectorEntrySchema(CustomSchema):
    class Meta:
        model = SectorEntry
        unknown =RAISE
        load_instance= True

class AssetsSectorSchema(CustomSchema):
    class Meta:
        model = AssetsSector
        unknwon =RAISE
        load_instance=True
        load_relationships =True
    
        
    sector_entry = Nested(SectorEntrySchema)
