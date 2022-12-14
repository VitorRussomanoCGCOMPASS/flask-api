from api.schemas.base_schema import CustomSchema
from api.models.currency import Currency, CurrencyValues
from marshmallow import RAISE, fields, pre_load, post_load


class CurrencySchema(CustomSchema):
    class Meta:
        model = Currency
        unknown = RAISE

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        return data

    @post_load
    def make_objects(self, data, **kwargs) -> Currency:
        return Currency(**data)


class CurrencyValuesSchema(CustomSchema):
    class Meta:
        model = CurrencyValues
        unknown = RAISE
        dateformat = "%Y-%m-%d"

    currency = fields.Nested(CurrencySchema)

    @post_load
    def make_objects(self, data, **kwargs) -> CurrencyValues:
        print(data)
        return CurrencyValues(**data)


# TODO : WE SHOULD USE RAISE FOR THE API
# TODO : WE SHOULD USE EXCLUDE FOR WEBSRAPPING. NEED TO MAKE THIS CHANGE WHEN CREATING AN INSTANCE OF THE SCHEMA!
