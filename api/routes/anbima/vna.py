from flask import Blueprint, jsonify, request

from api.models.vna import VNA
from api.request_schemas.dateargs import DateSchema, PeriodSchema
from api.routes.anbima import anbima_blueprint
from api.schemas.vna import VNASchema


@anbima_blueprint.route("/vna/", methods=["GET"])
def get_vna():

    """
    Returns all LFT, NTN-B and NTN-C market information. May be filtered by date or period.
    ---
    tags:
        - Anbima
    
    
    parameters:

      - name: date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
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
            type : array
            items:
                $ref: '#/definitions/VNA'
    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = VNA.query.filter_by(data_referencia=data_referencia).all()
        result = VNASchema().dump(result, many=True)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = VNA.query.filter(
            VNA.data_referencia.between(start_date, end_date)
        ).all()
        result = VNASchema().dump(result, many=True)
        return jsonify(result), 200

    result = VNA.query.all()
    result = VNASchema().dump(result, many=True)
    return jsonify(result), 200


@anbima_blueprint.route("/vna/<string:codigo_selic>", methods=["GET"])
def get_vna_id(codigo_selic: str):

    """
    Returns the data for a specific bond. May be further filtered by date or period.
    ---
    tags:
        - Anbima

    parameters:
      - name: codigo_selic
        in: path
        type: string
        required: False
        description:
            selic code of the bond.

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
                $ref: '#/definitions/VNA'
        '404':
          description: Bad Request. field `codigo_selic` must be a string.
    
    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = VNA.query.filter_by(
            data_referencia=data_referencia, codigo_selic=codigo_selic
        ).one_or_none()
        result = VNASchema().dump(result)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = (
            VNA.query.filter(VNA.data_referencia.between(start_date, end_date))
            .filter_by(codigo_selic=codigo_selic)
            .all()
        )
        result = VNASchema().dump(result, many=True)
        return jsonify(result), 200

    result = VNA.query.filter_by(codigo_selic=codigo_selic).all()
    result = VNASchema().dump(result, many=True)
    return jsonify(result), 200
