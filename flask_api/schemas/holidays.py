from flask_api.schemas.base_schema import CustomSchema
from flask_api.models.holidays import HolidayCalendars, Holidays
from marshmallow import RAISE

from marshmallow_sqlalchemy.fields import Nested


class HolidayCalendarsSchema(CustomSchema):
    class Meta:
        model = HolidayCalendars
        load_instance = True
        unknown = RAISE


class HolidaysSchema(CustomSchema):
    class Meta:
        model = Holidays
        dateformat = "%Y-%m-%d"
        load_instance = True
        load_relationships = True
        unknown = RAISE

    calendar = Nested(HolidayCalendarsSchema, required=True)
