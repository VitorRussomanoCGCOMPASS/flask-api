from marshmallow import Schema, fields, validates_schema, ValidationError


class DateargsSchema(Schema):
    
    class Meta:
        dateformat  = "%Y-%m-%d"
    
    
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)


    @validates_schema
    def validate_dates(self, data, **kwargs):
    
        if data['start_date'] >= data['end_date']:
            raise ValidationError("Start date should be greater than End date")
 