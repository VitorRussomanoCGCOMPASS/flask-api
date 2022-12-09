from api.request_schemas.dropargs import DropSchema
from marshmallow import fields, RAISE



class MarketIndexQuerySchema(DropSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    index = fields.String(allow_none=True)
    date = fields.String(allow_none=True)
