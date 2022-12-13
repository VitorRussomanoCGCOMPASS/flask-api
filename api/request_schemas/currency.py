from marshmallow import fields
from api.request_schemas.dateargs import DateSchema, PeriodSchema

class CurrencyDateQuerySchema(DateSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    currency_id = fields.Integer(data_key='id')

class CurrencyPeriodQuerySchema(PeriodSchema):
    class Meta:
        dateformat = "%Y-%m-%d"

    currency_id = fields.Integer(data_key='id')


