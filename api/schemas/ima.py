from marshmallow import EXCLUDE, post_load

from api.models.ima import IMA, ComponentsIMA
from api.schemas.base_schema import CustomSchema


class IMASchema(CustomSchema):
    class Meta:
        model = IMA
        unknown = EXCLUDE

    @post_load
    def post_loader(self, data, **kwargs):
        return IMA(**data)


class ComponentsIMASchema(CustomSchema):
    class Meta:
        model = ComponentsIMA
        unknown = EXCLUDE

    @post_load
    def post_loader(Self, data, **kwargs):
        return ComponentsIMA(**data)


