from marshmallow import fields, Schema, RAISE
from api.request_schemas.dropargs import DropSchema

class SectorQuerySchema(Schema):
    class Meta:
        unknown = RAISE
        
    methodology=  fields.String()
    

class AssetSectorQuerySchema(DropSchema):

    methodology = fields.String(allow_none=True)
    ticker= fields.String(allow_none=True)


