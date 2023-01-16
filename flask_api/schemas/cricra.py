from marshmallow import EXCLUDE, post_load

from flask_api.models.cricra import CriCra 
from flask_api.schemas.base_schema import CustomSchema


class CriCraSchema(CustomSchema):
    class Meta:
        model = CriCra
        unknown = EXCLUDE

    @post_load
    def make_objects(self, data, **kwargs):
        return CriCra(**data)
