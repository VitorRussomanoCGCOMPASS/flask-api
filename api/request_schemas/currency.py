from api.request_schemas.dropargs import DropSchema
from marshmallow import fields, RAISE
from api.request_schemas.dateargs import DateSchema, DateargsSchema

class CurrencyQuerySchema(DateSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    id = fields.Integer()

class CurrencyQueryArgsSchema(DateargsSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    id = fields.Integer()
