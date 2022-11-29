from marshmallow import Schema, fields, validates_schema, ValidationError


class DateargsSchema(Schema):
    
    class Meta:
        dateformat  = "%d-%m-%Y"
    
    
    start_date = fields.Date(required=True)
    end_date = fields.Date(allow_none=True)


    @validates_schema
    def validate_dates(self, data, **kwargs):
    
        if "end_date" in data and data['end_date'] is not None:
            if data['start_date'] >= data['end_date']:
                raise ValidationError("start date is later than end date")
 