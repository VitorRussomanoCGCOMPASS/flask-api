from flask import Blueprint, jsonify
from api.models.sector import SectorEntry
from api.schemas.sector import SectorEntrySchema
from flask import request

sector_blueprint = Blueprint("sector",__name__,url_prefix='/sector')
sectorentry_schema = SectorEntrySchema()



@sector_blueprint.route('/',methods=['GET'])
def get_sectorentry_bymethodology():
    args = request.args
    methodology = args.get('methodology')

    if methodology is not None:
        result = SectorEntry.query.filter_by(methodology=methodology).all()
    else:
        result = SectorEntry.query.all()

    if len(result) >1: 
        result =  sectorentry_schema.dump(result,many=True)
    else:
        result = sectorentry_schema.dump(result)

    return jsonify(result, 200)





