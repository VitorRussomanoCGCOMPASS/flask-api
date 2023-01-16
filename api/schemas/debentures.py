from marshmallow import EXCLUDE, RAISE, fields, post_load, pre_load

from api.models.debentures import AnbimaDebentures, Debentures, OtherDebentures
from api.schemas.base_schema import CustomSchema


# This is for the GET process from the Anbima API
class AnbimaDebenturesSchema(CustomSchema):
    """
    Serializer/Deserializer for AnbimaDebentures

    Methods:
    load()
        Deserializes the data
    dump()
        Serializes the data
    """

    class Meta:
        model = AnbimaDebentures
        unknown = EXCLUDE
        dateformat = "%Y-%m-%d"

    data_finalizado = fields.Date("%Y-%m-%dT%H:%M:%S.%f")

    @pre_load
    def pre_loader(self, data, many, **kwargs):
        """
        Pre processes the data. Exchanges '--' for None in percent_reune.
        """
        if data["percent_reune"] == "--":
            data["percent_reune"] = None
        else:
            data["percent_reune"] = float(data["percent_reune"].replace("%", "e-2"))
        return data

    @post_load
    def make_objets(self, data, **kwargs):
        return AnbimaDebentures(**data)


class DebenturesSchema(CustomSchema):
    class Meta:
        model = Debentures
        unknown = RAISE
        dateformat = "%Y-%m-%d"

    @post_load
    def make_objets(self, data, **kwargs):
        return Debentures(**data)


class OtherDebenturesSchema(CustomSchema):
    class Meta:
        model = OtherDebentures
        unknown = RAISE
        dateformat = "%Y-%m-%d"

    @post_load
    def make_objets(self, data, **kwargs):
        return OtherDebentures(**data)
