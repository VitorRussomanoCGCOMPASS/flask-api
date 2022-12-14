from flask import Blueprint, jsonify, request

from api.models.market_index import MarketIndex
from api.request_schemas.dateargs import DateSchema, PeriodSchema
from api.schemas.market_index import MarketIndexSchema

marketindex_blueprint = Blueprint("MarketIndex", __name__, url_prefix="/marketindex")


marketindex_schema = MarketIndexSchema()
dateargs_schema = PeriodSchema()


@marketindex_blueprint.route("/", methods=["GET"])
def get_marketindex():
    args = request.args
    if args:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad request", "message": error}), 400
        result = MarketIndex.query.filter_by(**args).all()
        result = marketindex_schema.dump(result, many=True)
        return jsonify(result), 200

    result = MarketIndex.query.all()
    result = marketindex_schema.dump(result, many=True)

    return jsonify(result), 200


@marketindex_blueprint.route("/<string:index>/", methods=["GET"])
def get_marketindex_id(index: str):

    """
    Market Index by date and or index.
    If no args, returns all data

    """
    args = request.args
    if args:
        errors = DateSchema().validate(args)
        if errors:
            return jsonify({"error": "Bad request", "message": errors}), 400

        result = MarketIndex.query.filter_by(**args, index=index).all()
        result = marketindex_schema.dump(result, many=True)
        return jsonify(result), 200

    result = MarketIndex.query.filter_by(index=index).all()
    result = marketindex_schema.dump(result, many=True)

    return jsonify(result), 200
