from marshmallow import EXCLUDE, post_load

from api.models.ima import IMA, ComponentsIMA
from api.schemas.base_schema import CustomSchema
from marshmallow import fields

from app import database



class IMASchema(CustomSchema):
    class Meta:
        model = IMA
        unknown = EXCLUDE
        load_instance= True
        sqla_session =database.session

class ComponentsIMASchema(CustomSchema):
    class Meta:
        model = ComponentsIMA
        unknown = EXCLUDE
        dateformat= "%Y-%m-%d"
        load_instance= True
        load_relationships =True
        
    index = fields.Nested(IMASchema)


