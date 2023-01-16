from api.schemas.base_schema import CustomSchema
from api.models.currency import Currency, CurrencyValues
from marshmallow import RAISE, fields, pre_load, post_load


from app import database


class CurrencySchema(CustomSchema):
    class Meta:
        model = Currency
        unknown = RAISE
        load_instance= True
        sqla_session = database.session

class CurrencyValuesSchema(CustomSchema):
    class Meta:
        model = CurrencyValues
        unknown = RAISE
        dateformat = "%Y-%m-%d"
        load_instance= True
        load_relationships = True
        
    currency = fields.Nested(CurrencySchema)
