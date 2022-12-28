from marshmallow import EXCLUDE, post_load

from api.models.cricra import CriCra 
from api.schemas.base_schema import CustomSchema


class CriCraSchema(CustomSchema):
    class Meta:
        model = CriCra
        unknown = EXCLUDE

    @post_load
    def make_objects(self, data, **kwargs):
        return CriCra(**data)
