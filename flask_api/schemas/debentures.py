from marshmallow import RAISE, post_load

from flask_api.models.debentures import Debentures
from flask_api.schemas.base_schema import CustomSchema


class DebenturesSchema(CustomSchema):
    class Meta:
        model = Debentures
        unknown = RAISE
        dateformat = "%Y-%m-%d"

    @post_load
    def make_objets(self, data, **kwargs):
        return Debentures(**data)
