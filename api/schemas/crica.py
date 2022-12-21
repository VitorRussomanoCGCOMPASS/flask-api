from marshmallow import EXCLUDE, post_load

from api.models.crica import Crica
from api.schemas.base_schema import CustomSchema


class CricaSchema(CustomSchema):
    class Meta:
        model = Crica
        unknown = EXCLUDE

    @post_load
    def make_objects(self, data, **kwargs):
        return Crica(**data)
