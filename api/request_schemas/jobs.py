from api.request_schemas.dropargs import DropSchema
from marshmallow import fields

class JobsQuerySchema(DropSchema):
    id = fields.String()
    