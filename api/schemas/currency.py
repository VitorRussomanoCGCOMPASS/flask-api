from api.schemas.base_schema import CustomSchema
from api.models.currency import Currency, CurrencyValues
from marshmallow import EXCLUDE, fields, pre_load, post_load


class CurrencySchema(CustomSchema):
    class Meta:
        model = Currency
        unknown = EXCLUDE

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        return data

    @post_load
    def make_objects(self, data, **kwargs) -> Currency:
        return Currency(**data)


class CurrencyValuesSchema(CustomSchema):
    class Meta:
        model = CurrencyValues
        unknown = EXCLUDE
        dateformat = "%Y-%m-%d"

    currency = fields.Nested(CurrencySchema)

    @post_load
    def make_objects(self, data, **kwargs) -> CurrencyValues:
        print(data)
        return CurrencyValues(**data)
