from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from api.models.currency import Currency, CurrencyValues
from api.request_schemas.dateargs import DateSchema, PeriodSchema

from api.schemas.currency import CurrencySchema, CurrencyValuesSchema
from app import database

currency_blueprint = Blueprint("Currency", __name__, url_prefix="/currencies")


#  TODO : REVIEW POST


@currency_blueprint.route("/", methods=["GET"])
def get_currency():

    result = Currency.query.all()
    result = CurrencySchema().dump(result, many=True)
    return jsonify(result), 200


@currency_blueprint.route("/<int:id>", methods=["GET"])
def get_currency_id(id: int):

    result = Currency.query.filter_by(id=id).one_or_404()
    result = CurrencySchema().dump(result)
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
            result = CurrencySchema().load(request.json)
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


@currency_blueprint.route("/<int:id>/values/", methods=["GET"])
def get_currency_values_id(id: int):
    args = request.args
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = CurrencyValues.query.filter_by(
            currency_id=id, date=date
        ).first_or_404()
        result = CurrencyValuesSchema()
        return jsonify(result), 200

    if end_date or start_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = (
            CurrencyValues.query.filter(
                CurrencyValues.date.between(start_date, end_date)
            )
            .filter_by(currency_id=id)
            .all()
        )
        try:
            result = CurrencyValuesSchema().dump(result, many=True)
        except ValueError:
            result = CurrencyValuesSchema().dump(result)
        return jsonify(result), 200

    result = CurrencyValues.query.filter_by(currency_id=id).all()
    try:
        result = CurrencyValuesSchema().dump(result, many=True)
    except ValueError:
        result = CurrencyValuesSchema().dump(result)
    return jsonify(result), 200


@currency_blueprint.route("/values/", methods=["GET"])
def get_currency_values_date():

    args = request.args
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = CurrencyValues.query.filter_by(date=date).one_or_404()
        result = CurrencyValuesSchema()
        return jsonify(result), 200

    if end_date or start_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = (
            CurrencyValues.query.filter(
                CurrencyValues.date.between(start_date, end_date)
            )
            .filter_by(currency_id=id)
            .all()
        )
        try:
            result = CurrencyValuesSchema().dump(result, many=True)
        except ValueError:
            result = CurrencyValuesSchema().dump(result)
        return jsonify(result), 200

    result = CurrencyValues.query.all()
    result = CurrencyValuesSchema()
    return jsonify(result), 200
