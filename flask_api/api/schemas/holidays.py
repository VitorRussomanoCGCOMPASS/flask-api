from api.schemas.base_schema import CustomSchema
from api.models.holidays import HolidayCalendars, Holidays
# from api.schemas.base_schema import SmartNested
from marshmallow import fields, RAISE

from app import database


class HolidayCalendarsSchema(CustomSchema):
    class Meta:
        model = HolidayCalendars
        load_instance=True
        sqla_session =database.session 
        unknown =RAISE
      
class HolidaysSchema(CustomSchema):
    class Meta:
        model = Holidays
        dateformat = "%Y-%m-%d"
        load_instance= True
        load_relationships = True
        unknown =RAISE
    
    calendar = fields.Nested(HolidayCalendarsSchema,required=True)


 