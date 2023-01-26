from flask_api.schemas.base_schema import CustomSchema
from flask_api.models.currency import Currency, CurrencyValues
from marshmallow import RAISE, pre_load, post_load
from marshmallow_sqlalchemy.fields import Nested


class CurrencySchema(CustomSchema):
    class Meta:
        model = Currency
        unknown = RAISE
        load_instance = True


class CurrencyValuesSchema(CustomSchema):
    class Meta:
        model = CurrencyValues
        unknown = RAISE
        dateformat = "%Y-%m-%d"
        load_instance = True
        load_relationships = True

    currency = Nested(CurrencySchema)
