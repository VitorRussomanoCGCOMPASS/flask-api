from marshmallow import EXCLUDE, post_load

from flask_api.models.ima import IMA, ComponentsIMA
from flask_api.schemas.base_schema import CustomSchema
from marshmallow import fields


from marshmallow_sqlalchemy.fields import Nested


class ComponentsIMASchema(CustomSchema):
    class Meta:
        model = ComponentsIMA
        unknown = EXCLUDE
        dateformat = "%Y-%m-%d"
        load_instance = True
        include_relationships = False
        include_fk = True


class IMASchema(CustomSchema):
    class Meta:
        model = IMA
        unknown = EXCLUDE
        load_instance = True
        load_relationships = False
        include_relationships = False
        include_fk = False
        dateformat = "%Y-%m-%d"

    yield_col = fields.Float(data_key="yield")
    components = Nested(ComponentsIMASchema, data_key="componentes", many=True)
