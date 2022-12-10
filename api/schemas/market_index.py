from marshmallow import EXCLUDE, post_load, pre_load

from api.models.market_index import MarketIndex
from api.schemas.base_schema import CustomSchema

# This Schema allows for deserialization from B3 website
class MarketIndexSchema(CustomSchema):
    class Meta:
        model = MarketIndex
        unknown = EXCLUDE
        dateformat = "%Y-%m-%d"

    @pre_load(pass_many=True)
    def pre_lds(self, data, many, **kwargs):
        return data

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        data["part"] = float(data["part"].replace(",", "."))
        data["theoricalQty"] = float(data["theoricalQty"].replace(".", ""))
        if self.context:
            data["date"] = self.context.get("date")
            data["index"] = self.context.get("index")

        return data

    @post_load
    def make_objects(self, data, many, **kwargs):
        return MarketIndex(**data)