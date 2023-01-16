from marshmallow import RAISE, post_load

from api.models.eventlog import EventLog
from api.schemas.base_schema import CustomSchema


class EventLogSchema(CustomSchema):
    class Meta:
        model = EventLog
        unknown = RAISE

    @post_load
    def post_loader(self, data, **kwargs) -> EventLog:
        return EventLog(**data)
