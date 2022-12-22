from marshmallow import RAISE, fields, post_load, pre_load

from api.models.indexes import Indexes, IndexValues
from api.schemas.base_schema import CustomSchema


# TODO: SHOULD NOT BE THIS ONE PRE_LOADER, IT IS SPECIFIC FOR CDI
# TODO; RENAME THE TABLE


class IndexesSchema(CustomSchema):
    class Meta:
        model = Indexes
        unknown = RAISE

    @post_load
    def make_object(self, data, **kwargs) -> Indexes:
        return Indexes(**data)


class IndexValuesSchema(CustomSchema):
    class Meta:
        model = IndexValues
        unknown = RAISE
        dateformat = "%Y-%m-%d"

    index = fields.Nested(IndexesSchema)

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        return data

    @post_load
    def make_object(self, data, **kwargs) -> IndexValues:
        return IndexValues(**data)


class CDIValueSchema(IndexValuesSchema):
    @pre_load
    def pre_loader(self, data, many, **kwargs):
        data["date"] = data["date"].rpartition("T")[0]
        return data

