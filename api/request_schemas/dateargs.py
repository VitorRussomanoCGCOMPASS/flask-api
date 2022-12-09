"""  Validate query arguments with dates """
from marshmallow import RAISE, Schema, ValidationError, fields, validates_schema
from api.request_schemas.dropargs import DropSchema

class DateargsSchema(DropSchema):
    class Meta:
        dateformat = "%Y-%m-%d"
        unknown = RAISE

    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    @validates_schema
    def validate_dates(self, data, **kwargs):

        if data["start_date"] >= data["end_date"]:
            raise ValidationError("Start date should be greater than End date")


class DateSchema(DropSchema):
    class Meta:
        dateformat = "%Y-%m-%d"
        unknown = RAISE

    date = fields.Date(required=True)


