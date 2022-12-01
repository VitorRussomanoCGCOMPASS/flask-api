from api.models.sector import SectorEntry , AssetsSector
from api.schemas.base_schema import CustomSchema
from marshmallow import fields, pre_load, post_load, EXCLUDE



class SectorEntrySchema(CustomSchema): 
    class Meta:
        model = SectorEntry 
        unknown = EXCLUDE 

    @pre_load
    def pre_loader(self, data ,many, **kwargs):
        return data

    @post_load
    def post_loader(self, data, **kwargs) -> SectorEntry:
        return SectorEntry(**data) 



class AssetsSectorSchema(CustomSchema):
    class Meta:
        model = AssetsSector
        unknown = EXCLUDE

    sector_entry = fields.Nested(SectorEntrySchema)

    @pre_load
    def pre_loader(self, data ,many, **kwargs):
        return data

    @post_load
    def post_loader(self, data, **kwargs) -> AssetsSector:
        return AssetsSector(**data) 



A = {"sector_entry" : { 'sector':'ABC', 'subsector':'D', 'methodology':"TESTE"} , 'ticker':"ticker"}

scm = AssetsSectorSchema()    
K = scm.load(A)