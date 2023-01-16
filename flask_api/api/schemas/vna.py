from marshmallow import EXCLUDE, post_load
from api.models.vna import VNA
from api.schemas.base_schema import CustomSchema


class VNASchema(CustomSchema):
    class Meta:
        model = VNA
        unknown = EXCLUDE

    @post_load
    def post_loader(self, data, **kwargs):
        return VNA(**data)
