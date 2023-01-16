from marshmallow import RAISE, post_load

from flask_api.models.eventlog import EventLog
from flask_api.schemas.base_schema import CustomSchema


class EventLogSchema(CustomSchema):
    class Meta:
        model = EventLog
        unknown = RAISE

    @post_load
    def post_loader(self, data, **kwargs) -> EventLog:
        return EventLog(**data)
