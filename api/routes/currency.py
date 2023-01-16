from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from api.models.currency import Currency, CurrencyValues
from api.request_schemas.dateargs import DateSchema, PeriodSchema

from api.schemas.currency import CurrencySchema, CurrencyValuesSchema

from app import database


currency_blueprint = Blueprint("Currency", __name__, url_prefix="/currencies")


@currency_blueprint.route("/", methods=["GET"])
def get_currency():
    """
    Returns all Currencies
    ---

    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/Currency'

    """
    result = database.session.query(Currency).all()
    result = CurrencySchema().dump(result, many=True)
    return jsonify(result), 200


@currency_blueprint.route("/<int:id>", methods=["GET"])
def get_currency_id(id: int):
    """
    Returns the Currency associated with the provided ID
    ---

    parameters:
      - name: id
        in: path
        type: integer
        required: False

    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/Currency'

        '404':
          description: Bad Request. field `id` must be an integer
    """
    result = database.session.query(Currency).filter_by(id=id).one_or_none()
    #     result = Currency.query.filter_by(id=id).one_or_none()
    result = CurrencySchema().dump(result)
    return jsonify(result), 200


@currency_blueprint.route("/", methods=["POST"])
def post_currency():
    """

    Posts a new Currency
    ---


    consumes:
        - application/json

    parameters:
        - in: body
          name: currency
          description: The new currency to create
          schema:
                $ref: '#/definitions/Currency'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/Currency'

        '400':
            description: Bad Request
    """
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )

    if not request.json:
        return (jsonify({"error": "Bad Request", "message": "Empty data"}), 400)

    try:
        result = CurrencySchema().load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    if "id" in request.json:
        id = request.json["id"]
        existing_currency = Currency.query.filter_by(id=id).one_or_none()
        if existing_currency:
            return (
                jsonify(
                    {
                        "error": "Bad Request",
                        "message": f"Currency: with id {id} already exists",
                    }
                ),
                400,
            )
    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200


def get_currency_period(start_date, end_date, currency_id):

    if currency_id:
        result = (
            CurrencyValues.query.filter(
                CurrencyValues.date.between(start_date, end_date)
            )
            .filter_by(currency_id=currency_id)
            .all()
        )

    else:
        result = CurrencyValues.query.filter(
            CurrencyValues.date.between(start_date, end_date)
        ).all()

    result = CurrencyValuesSchema().dump(result, many=True)
    return result


def get_currency_date(date, currency_id):

    if currency_id:
        result = CurrencyValues.query.filter_by(
            currency_id=currency_id, date=date
        ).one_or_none()
        result = CurrencyValuesSchema().dump(result)

    else:
        result = CurrencyValues.query.filter_by(date=date).all()
        result = CurrencyValuesSchema().dump(result, many=True)

    return result


@currency_blueprint.route("/<int:id>/values/", methods=["GET"])
def get_currency_values_id(id: int):
    """
    Returns all values associated with a Currency. May be filtered down by date or period.
    ---

    parameters:
      - name: id
        in: path
        type: integer
        required: False

      - name: date
        in: query
        type: string
        required: False
        format:  'YYYY-mm-dd'
        description:
            The date of the values to filter by.
            This parameter is incompatible with `start_date` and `end_date`.

      - name: start_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The start_date for the period of which the values will be filtered. Must be used together with `end_date`.
            This parameter is incompatible with `date`.

      - name: end_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The end_date for the period of which the values will be filtered. Must be used together with `start_date`.
            This parameter is incompatible with `date`.

    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/CurrencyValues'

        '400':
          description: Bad Request

        '404':
          description: Bad Request. field `id` must be integer
    """
    args = request.args
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_currency_date(date, id)
        return jsonify(result), 200

    if end_date or start_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_currency_period(start_date, end_date, id)
        return jsonify(result), 200

    result = database.session.query(CurrencyValues).filter_by(currency_id=id).all()
    #   result = CurrencyValues.query.filter_by(currency_id=id).all()
    result = CurrencyValuesSchema().dump(result, many=True)
    return jsonify(result), 200


@currency_blueprint.route("/values/", methods=["GET"])
def get_currency_values_date():
    """
    Returns all values associated with all Currencies. May be filtered down by date or period.

    ---
    parameters:
      - name: date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            This parameter is incompatible with `start_date` and `end_date`.


      - name: start_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The start_date for the period of which the values will be filtered. Must be used together with `end_date`.
            This parameter is incompatible with `date`.

      - name: end_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The end_date for the period of which the values will be filtered. Must be used together with `start_date`.
            This parameter is incompatible with `date`.

    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/CurrencyValues'

        '400':
          description: Bad Request


    """
    args = request.args
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_currency_date(date, currency_id=None)
        return jsonify(result), 200

    if end_date or start_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_currency_period(start_date, end_date, currency_id=None)
        return jsonify(result), 200
    result = database.session.query(CurrencyValues).all()
    result = CurrencyValuesSchema().dump(result, many=True)
    return jsonify(result), 200


@currency_blueprint.route("/values/", methods=["POST"])
def post_currency_values():

    """
    Posts a new value to a currency
    ---

    consumes:
        - application/json

    parameters:
        - in: body
          name: currency value
          description: A value to entry associated with a currency
          schema:
                $ref: '#/definitions/CurrencyValues'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/CurrencyValues'

        '400':
            description: Bad Request
    """
    content_type = request.headers.get("Content-Type")

    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )

    if not request.json:
        return (jsonify({"error": "Bad Request", "message": "Empty data"}), 400)

    try:
        result = CurrencyValuesSchema(session=database.session).load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    currency = request.json["currency"]["currency"]
    existing_currency = Currency.query.filter_by(currency=currency).one_or_none()

    if existing_currency:
        request.json["currency"] = CurrencySchema().dump(existing_currency)
        result = CurrencyValuesSchema(session=database.session).load(request.json)

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200
