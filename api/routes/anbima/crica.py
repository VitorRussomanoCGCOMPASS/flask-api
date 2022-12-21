from flask import Blueprint, jsonify, request

from api.models.crica import Crica
from api.routes.anbima import anbima_blueprint
from api.schemas.crica import CricaSchema

from api.request_schemas.dateargs import DateSchema, PeriodSchema


def get_crica_period(start_date, end_date, emissor=None, codigo_ativo=None):
    if codigo_ativo:
        result = (
            Crica.query.filter(Crica.data_referencia.between(start_date, end_date))
            .filter_by(codigo_ativo=codigo_ativo)
            .all()
        )
    elif emissor:
        result = (
            Crica.query.filter(Crica.data_referencia.between(start_date, end_date))
            .filter_by(emissor=emissor)
            .all()
        )
    else:
        result = Crica.query.filter(
            Crica.data_referencia.between(start_date, end_date)
        ).all()

    try:
        result = CricaSchema().dump(result, many=True)
    except TypeError:
        result = CricaSchema().dump(result)
    return result


def get_crica_date(data_referencia, emissor=None, codigo_ativo=None):
    if codigo_ativo:
        result = Crica.query.filter_by(
            data_referencia=data_referencia, codigo_ativo=codigo_ativo
        ).one()

    elif emissor:
        result = Crica.query.filter_by(
            data_referencia=data_referencia, emissor=emissor
        ).all()
    else:
        result = Crica.query.filter_by(data_referencia=data_referencia).all()
    try:
        result = CricaSchema().dump(result, many=True)
    except TypeError:
        result = CricaSchema().dump(result)
    return result


@anbima_blueprint.route("/crica/", methods=["GET"])
def get_crica():
    """
    Returns the bid, ask and indicative rates as well as Unit Prices corresponding to the real state and agribusiness recievables calculated by Anbima. May be filtered down by date or period.
    ---
    tags:
        - Anbima

    parameters:

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
                $ref: '#/definitions/Crica'
              
        '400':
          description: Bad Request
    """
    args = request.args

    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_crica_date(data_referencia=data_referencia)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_crica_period(start_date=start_date, end_date=end_date)
        return jsonify(result), 200

    result = Crica.query.all()
    try:
        result = CricaSchema().dump(result, many=True)
    except TypeError:
        result = CricaSchema().dump(result)
    return jsonify(result), 200

@anbima_blueprint.route("/crica/<string:codigo_ativo>", methods=["GET"])
def get_crica_cod(codigo_ativo:str):
    
    """
    Returns the bid, ask and indicative rates as well as Unit Prices corresponding to a real state and agribusiness recievable given the `codigo_ativo`. May be filtered further down by date or period.
    ---
    tags:
        - Anbima

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
                $ref: '#/definitions/Crica'
              
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
        result = get_crica_date(data_referencia=data_referencia,codigo_ativo=codigo_ativo)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_crica_period(start_date=start_date, end_date=end_date,codigo_ativo=codigo_ativo)
        return jsonify(result), 200

    result = Crica.query.all()
    try:
        result = CricaSchema().dump(result, many=True)
    except TypeError:
        result = CricaSchema().dump(result)
    return jsonify(result), 200

@anbima_blueprint.route("/crica/<string:issuer>", methods=["GET"])
def get_crica_emissor(issuer:str):
        
    """
    Returns the bid, ask and indicative rates as well as Unit Prices corresponding to the real state and agribusiness recievable given the issuer. May be filtered further down by date or period.
    ---
    tags:
        - Anbima

    parameters:
      - name: issuer
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
                $ref: '#/definitions/Crica'
              
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
        result = get_crica_date(data_referencia=data_referencia,emissor=issuer)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_crica_period(start_date=start_date, end_date=end_date,emissor=issuer)
        return jsonify(result), 200

    result = Crica.query.all()
    try:
        result = CricaSchema().dump(result, many=True)
    except TypeError:
        result = CricaSchema().dump(result)
    return jsonify(result), 200
