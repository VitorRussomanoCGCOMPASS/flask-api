from marshmallow import EXCLUDE, post_load

from api.models.ima import IMA, ComponentsIMA
from api.schemas.base_schema import CustomSchema
from marshmallow import fields



class IMASchema(CustomSchema):
    class Meta:
        model = IMA
        unknown = EXCLUDE


    @post_load
    def post_loader(self, data, **kwargs) -> IMA:
        return IMA(**data)

class ComponentsIMASchema(CustomSchema):
    class Meta:
        model = ComponentsIMA
        unknown = EXCLUDE

    index = fields.Nested(IMASchema)


    @post_load
    def post_loader(Self, data, **kwargs) -> ComponentsIMA:
        return ComponentsIMA(**data)
