from api.schemas.base_schema import CustomSchema
from api.models.holidays import HolidayCalendars, Holidays
# from api.schemas.base_schema import SmartNested
from marshmallow import fields

from app import database


class HolidayCalendarsSchema(CustomSchema):
    class Meta:
        model = HolidayCalendars
        load_instance=True
        sqla_session =database.session 
      
class HolidaysSchema(CustomSchema):
    class Meta:
        model = Holidays
        dateformat = "%Y-%m-%d"
        load_instance= True
        load_relationships = True
        sqla_session= database.session
    
    calendar = fields.Nested(HolidayCalendarsSchema,required=True)


 