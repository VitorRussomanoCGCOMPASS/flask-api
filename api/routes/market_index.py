from flask import Blueprint, jsonify, request
from api.models.market_index import MarketIndex
from api.schemas.market_index import MarketIndexSchema
from api.schemas.dateargs import DateargsSchema

marketindex_blueprint = Blueprint("MarketIndex", __name__, url_prefix="/marketindex")


marketindex_schema = MarketIndexSchema()
dateargs_schema = DateargsSchema()


@marketindex_blueprint.route("/", methods=["GET"])
def get_marketindex():
    args = request.args

    index = args.get("index", type=str)

    if not index:
        result = MarketIndex.query.all()
        result = marketindex_schema.dump(result, many=True)
        return jsonify(result), 200

    if index:
        result = MarketIndex.query.filter_by(index=index)
        result = marketindex_schema.dump(result, many=True)
        return jsonify(result), 200

    return jsonify({"error": "Bad Request", "message": "#####"}), 400


@marketindex_blueprint.route("/date", methods=["GET"])
def get_marketindex_date():
    args = request.args
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)
    
    errors = dateargs_schema.validate({"start_date": start_date, "end_date": end_date})
    if errors:
        return jsonify({"error":"Bad Request", "message":errors}) , 400

    result = MarketIndex.query.filter(MarketIndex.date.between(start_date,end_date)).all()  

    result = marketindex_schema.dump(result,many=True)
    return jsonify(result), 200


""" 

    result = MarketIndex.query.filter_by(index=index).all()
    try:
        result = marketindex_schema.dump(result, many=True)
    except ValueError:
        result = marketindex_schema.dump(result)
    return jsonify(result), 200


 """
