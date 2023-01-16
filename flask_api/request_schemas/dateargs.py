"""  Validate query arguments with dates """
from marshmallow import RAISE, ValidationError, fields, validates_schema
from flask_api.request_schemas.add_fields import AdditionalFieldsSchema



class PeriodSchema(AdditionalFieldsSchema):
    class Meta:
        dateformat = "%Y-%m-%d"
        unknown = RAISE
    
 
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    @validates_schema
    def validate_dates(self, data, **kwargs):

        if data["start_date"] >= data["end_date"]:
            raise ValidationError("Start date should be greater than End date")


class DateSchema(AdditionalFieldsSchema):
    class Meta:
        dateformat = "%Y-%m-%d"
        unknown = RAISE

    date = fields.Date(required=True)
