from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from api.models.currency import Currency, CurrencyValues
from api.request_schemas.currency import (
    CurrencyPeriodQuerySchema,
    CurrencyDateQuerySchema,
)
from api.schemas.currency import CurrencySchema, CurrencyValuesSchema
from app import database

currency_blueprint = Blueprint("Currency", __name__, url_prefix="/currencies")

currency_schema = CurrencySchema()
currency_values_schema = CurrencyValuesSchema()


@currency_blueprint.route("/", methods=["GET"])
def get_currency():

    result = Currency.query.all()
    result = currency_schema.dump(result, many=True)
    return jsonify(result), 200


@currency_blueprint.route("/", methods=["POST"])
def post_currency():
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:
        try:
            result = currency_schema.load(request.json)
        except ValidationError as err:
            return jsonify({"error": "Bad Request", "message": err.messages}), 400
        try:
            database.session.add(result)
            database.session.commit()
        except Exception as exc:
            return (
                jsonify({"error": "Server Unavailable", "message": "######"}),
                400,
            )

    return jsonify(request.json), 200


def get_currency_period(start_date, end_date, currency_id):
    result = (
        CurrencyValues.query.filter(CurrencyValues.date.between(start_date, end_date))
        .filter_by(currency_id=currency_id)
        .all()
    )
    try:
        result = currency_values_schema.dump(result, many=True)
    except ValueError:
        result = currency_values_schema.dump(result)
    return result


@currency_blueprint.route("/values/", methods=["GET"])
def get_currency_values_date():

    args = request.args
    currency_id = args.get("id", type=int)
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = CurrencyDateQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = CurrencyValues.query.filter_by(
            currency_id=currency_id, date=date
        ).first_or_404()
        result = currency_values_schema.dump(result)
        return jsonify(result), 200

    if end_date or start_date:
        error = CurrencyPeriodQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_currency_period(start_date, end_date, currency_id)
        return jsonify(result), 200

    if currency_id is not None:
        result = CurrencyValues.query.filter_by(currency_id=currency_id).all()
        try:
            result = currency_values_schema.dump(result, many=True)
        except ValueError:
            result = currency_schema.dump(result)
        return jsonify(result), 200

    result = CurrencyValues.query.all()
    result = currency_values_schema.dump(result, many=True)
    return jsonify(result), 200
