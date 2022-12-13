from marshmallow import fields
from marshmallow import Schema

class HolidaysQuerySchema(Schema):
    calendar_id = fields.Integer(data_key='id')

