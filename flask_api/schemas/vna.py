from marshmallow import EXCLUDE, post_load
from flask_api.models.vna import VNA
from flask_api.schemas.base_schema import CustomSchema


class VNASchema(CustomSchema):
    class Meta:
        model = VNA
        unknown = EXCLUDE

    @post_load
    def post_loader(self, data, **kwargs):
        return VNA(**data)
