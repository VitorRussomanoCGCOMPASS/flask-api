from flask import Blueprint, jsonify, request
from api.models.currency import CurrencyValues, Currency
from api.schemas.currency import CurrencySchema, CurrencyValuesSchema
from api.request_schemas.currency import CurrencyQueryArgsSchema, CurrencyQuerySchema
import datetime


currency_blueprint = Blueprint("Currency", __name__, url_prefix="/currency")

currency_schema = CurrencySchema()
currency_values_schema = CurrencyValuesSchema()


@currency_blueprint.route("/", methods=["GET"])
def get_currency():
    if request.method == "GET":
        result = Currency.query.all()
        result = currency_schema.dump(result, many=True)
        return jsonify(result), 200
    if request.method == "POST":
        return jsonify({"error": "Not implemented"}), 400
    return (
        jsonify(
            {
                "error": "Bad Request",
                "message": "Function not implemented. Try GET or POST",
            }
        ),
        400,
    )


@currency_blueprint.route("/", methods=["GET"])
def get_currency_values_date():
    args = request.args
    id = args.get("id", type=int)
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = CurrencyQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400

        result = CurrencyValues.query.filter_by(**args).all()
        result = currency_values_schema.dump(result)
        return jsonify(result), 200

    if end_date or start_date:
        error = CurrencyQueryArgsSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = (
            CurrencyValues.query.filter(
                CurrencyValues.date.between(start_date, end_date)
            )
            .filter_by(id=id)
            .all()
        )
        try:
            result = currency_values_schema.dump(result, many=True)
        except ValueError:
            result = currency_values_schema.dump(result)
        return jsonify(result), 200

    result = CurrencyValues.query.all()
    result = currency_values_schema.dump(result, many=True)
    return jsonify(result), 200
