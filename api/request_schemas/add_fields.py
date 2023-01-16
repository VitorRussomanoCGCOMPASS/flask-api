from marshmallow import RAISE, Schema, ValidationError, fields, validates_schema


class AdditionalFieldsSchema(Schema):
    
    def __init__(self, additional_fields=None, **kwargs):
        super().__init__(**kwargs)
        if additional_fields:
            self.declared_fields.update(additional_fields)

 
if __name__ == '__main__':
    additional_fields = {"foo": fields.Int()}
    sch = AdditionalFieldsSchema(additional_fields=additional_fields)
    print(sch.declared_fields)



