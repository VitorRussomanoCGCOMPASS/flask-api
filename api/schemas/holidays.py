from api.schemas.base_schema import CustomSchema
from api.models.holidays import HolidayCalendars, Holidays
from marshmallow import fields, pre_load, post_load
from api.schemas.base_schema import SmartNested



class HolidayCalendarsSchema(CustomSchema):
    class Meta:
        model = HolidayCalendars
        load_instance= True
        include_relationships = True

        
class HolidaysSchema(CustomSchema):
    class Meta:
        model = Holidays
        include_fk = True
        load_instance = True
        dateformat = "%Y-%m-%d"
    
    calendar =  SmartNested(HolidayCalendarsSchema)
    
