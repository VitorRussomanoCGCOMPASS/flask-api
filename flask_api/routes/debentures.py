from flask import Blueprint, jsonify, request
from marshmallow import ValidationError, fields

from flask_api.models.debentures import Debentures, OtherDebentures
from flask_api.schemas.debentures import DebenturesSchema, OtherDebenturesSchema
from flask_api.app import database
from flask_api.request_schemas.dateargs import DateSchema, PeriodSchema

debentures_blueprint = Blueprint("Debentures", __name__, url_prefix="/debentures")


def get_debentures_date(date, issuer=None, codigo_ativo=None):

    if issuer:
        result =database.session.query(Debentures).filter_by(
            data_referencia=date, issuer=issuer
        ).one_or_none()
        result = DebenturesSchema().dump(result)
        return result
    
    elif codigo_ativo:
        result =database.session.query(Debentures).filter_by(
            data_referencia=date, codigo_ativo=codigo_ativo
        ).all()
    else:
        result =database.session.query(Debentures).filter_by(data_referencia=date).all()

    result = DebenturesSchema().dump(result, many=True)
    return result


def get_debentures_period(start_date, end_date, issuer=None, codigo_ativo=None):
    if issuer:
        result = (
           database.session.query(Debentures).filter(
                Debentures.data_referencia.between(start_date, end_date)
            )
            .filter_by(issuer=issuer)
            .all()
        )
    if codigo_ativo:
        result = (
           database.session.query(Debentures).filter(
                Debentures.data_referencia.between(start_date, end_date)
            )
            .filter_by(codigo_ativo=codigo_ativo)
            .all()
        )
    else:
        result =database.session.query(Debentures).filter(
            Debentures.data_referencia.between(start_date, end_date)
        ).all()

    result = DebenturesSchema().dump(result, many=True)
    return result


@debentures_blueprint.route("/", methods=["GET"])
def get_debentures():
    """
    Returns all debentures bid, ask and indicative rates as well as Unit Prices
    ---
    parameters:

      - name: issuer
        in: query
        type: string
        required: False
        description:
            Securitization company responsible for issuing the paper

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
                $ref : '#/definitions/AnbimaDebentures'

        '400':
          description: Bad Request
    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)
    issuer = args.get("issuer", type=str)

    if data_referencia:
        error = DateSchema({"issuer": fields.Str()}).validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400

        result = get_debentures_date(**args)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema({"issuer": fields.Str()}).validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400

        result = get_debentures_period(**args)
        return jsonify(result), 200

    if issuer:
        result =database.session.query(Debentures).filter_by(emissor=issuer).all()
    else:
        result =database.session.query(Debentures).all()

    result = DebenturesSchema().dump(result, many=True)
    return jsonify(result), 200


@debentures_blueprint.route("/<string:codigo_ativo>", methods=["GET"])
def get_debentures_cod(codigo_ativo: str):
    """
    Returns all debentures bid, ask and indicative rates as well as Unit Prices
    ---


    parameters:
      - name: codigo_ativo
        in: path
        type: string
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
                $ref : '#/definitions/AnbimaDebentures'

        '400':
          description: Bad Request

        '404':
          description: Bad Request. field `codigo_ativo` must be string

    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400

        args["codigo_ativo"] = codigo_ativo
        result = get_debentures_date(**args)

        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400

        args["codigo_ativo"] = codigo_ativo
        result = get_debentures_period(**args)

    result =database.session.query(Debentures).filter_by(codigo_ativo=codigo_ativo).all()
    result = DebenturesSchema().dump(result, many=True)
    return jsonify(result), 200


@debentures_blueprint.route("/", methods=["POST"])
def post_debentures():
    """
    Posts a new value to a non-anbima calculated bonds (debentures)

    ---

    consumes:
        - application/json

    parameters:
        - in: body
          name: debenture
          schema:
                $ref: '#/definitions/OtherDebentures'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/OtherDebentures'

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
        result = OtherDebenturesSchema().load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200


@debentures_blueprint.route("/<string:codigo_ativo>", methods=["PUT"])
def update_debentures(codigo_ativo: str):
    args = request.args
    data_referencia = args.get("date", type=str)

    content_type = request.headers.get("Content-Type")

    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )

    if not request.json:
        return (jsonify({"error": "Bad Request", "message": "Empty data"}), 400)

    error = DateSchema().validate(args)

    if error:
        return jsonify({"error": "Bad Request", "message": error}), 400

    existing_debenture =database.session.query(Debentures).filter_by(
        codigo_ativo=codigo_ativo, data_referencia=data_referencia
    ).one_or_none()
    if existing_debenture:
        existing_debenture = DebenturesSchema().dump(existing_debenture)
        existing_debenture.__dict__.update(request.json)

        try:
            updated_debenture = DebenturesSchema().load(existing_debenture)
        except ValidationError as err:
            return jsonify({"error": "Bad Request", "message": err.messages}), 400

        database.session.merge(updated_debenture)
        database.session.commit()
        return jsonify(existing_debenture), 200
    return (
        jsonify(
            {
                "error": "Bad Request",
                "message": f"Debenture with data_referencia : {data_referencia} and codigo_ativo : {codigo_ativo} not found",
            }
        ),
        400,
    )
