from api.models.sector import SectorEntry , AssetsSector
from api.schemas.base_schema import CustomSchema
from marshmallow import RAISE, fields


class SectorEntrySchema(CustomSchema):
    class Meta:
        model = SectorEntry 
        unknown = RAISE

class AssetsSectorSchema(CustomSchema):
    class Meta:
        model = AssetsSector
        unknown = RAISE

    sector_entry = fields.Nested(SectorEntrySchema)