from api.schemas.base_schema import CustomSchema
from api.models.holidays import HolidayCalendars, Holidays
from marshmallow import fields, pre_load, post_load


class HolidayCalendarsSchema(CustomSchema):
    class Meta:
        model = HolidayCalendars

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        return data

    @post_load
    def make_objects(self, data, **kwargs) -> HolidayCalendars:
        return HolidayCalendars(**data)


class HolidaysSchema(CustomSchema):
    class Meta:
        model = Holidays

    id= fields.Nested(HolidayCalendarsSchema, only=("id",))

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        return data

    @post_load
    def make_objects(self, data, **kwargs):
        return Holidays(**data)