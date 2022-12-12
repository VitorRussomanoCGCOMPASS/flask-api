from marshmallow import fields
from api.request_schemas.dateargs import DateSchema, DateargsSchema

class CurrencyDateQuerySchema(DateSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    currency_id = fields.Integer(data_key='id')

class CurrencyPeriodQuerySchema(DateargsSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    currency_id = fields.Integer(data_key='id')


