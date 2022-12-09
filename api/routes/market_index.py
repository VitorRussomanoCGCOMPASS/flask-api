from flask import Blueprint, jsonify, request
from api.models.market_index import MarketIndex
from api.schemas.market_index import MarketIndexSchema
from api.request_schemas.dateargs import DateargsSchema
from api.request_schemas.marketindex import MarketIndexQuerySchema


marketindex_blueprint = Blueprint("MarketIndex", __name__, url_prefix="/marketindex")


marketindex_schema = MarketIndexSchema()
dateargs_schema = DateargsSchema()


@marketindex_blueprint.route("/", methods=["GET"])
def getmarketindex_date():
    args = request.args
    errors = MarketIndexQuerySchema().validate(args)

    if errors:
        return jsonify({"error": "Bad request", "message": errors}), 400

    args = MarketIndexQuerySchema().dump(args)
    result = MarketIndex.query.filter_by(**args).all()
    result = marketindex_schema.dump(result, many=True)
    return jsonify(result), 200
