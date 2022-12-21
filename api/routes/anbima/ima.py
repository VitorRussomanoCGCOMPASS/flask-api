from flask import Blueprint, jsonify, request

from api.models.ima import IMA, ComponentsIMA
from api.routes.anbima import anbima_blueprint
from api.schemas.ima import ComponentsIMASchema, IMASchema
from api.request_schemas.dateargs import DateSchema, PeriodSchema


def get_ima_date(data_referencia, indice=None):
    if indice:
        result = IMA.query.filter_by(
            data_referencia=data_referencia, indice=indice
        ).one()
    else:
        result = IMA.query.filter_by(data_referencia=data_referencia).all()
    try:
        result = IMASchema().dump(result, many=True)
    except TypeError:
        result = IMASchema().dump(result)
    return result


def get_ima_period(start_date, end_date, indice=None):
    if indice:
        result = IMA.query.filter(
            IMA.data_referencia.between(start_date, end_date)
        ).all()
    else:
        result = IMA.query.filter(
            IMA.data_referencia.between(start_date, end_date)
        ).all()
    try:
        result = IMASchema().dump(result, many=True)
    except TypeError:
        result = IMASchema().dump(result)
    return result


def get_comp_date(data_referencia, indice=None):
    if indice:
        result = ComponentsIMA.query.filter_by(
            data_referencia=data_referencia, indice=indice
        ).one()
    else:
        result = ComponentsIMA.query.filter_by(data_referencia=data_referencia).all()
    try:
        result = ComponentsIMA().dump(result, many=True)
    except TypeError:
        result = ComponentsIMA().dump(result)
    return result


def get_comp_period(start_date, end_date, indice=None):
    if indice:
        result = ComponentsIMA.query.filter(
            ComponentsIMA.data_referencia.between(start_date, end_date)
        ).all()
    else:
        result = ComponentsIMA.query.filter(
            ComponentsIMA.data_referencia.between(start_date, end_date)
        ).all()
    try:
        result = ComponentsIMASchema().dump(result, many=True)
    except TypeError:
        result = ComponentsIMASchema().dump(result)
    return result



@anbima_blueprint.route("/ima/", methods=["GET"])
def get_ima():
    """
    Returns all results of IMA-related indexes. May be filtered down by date or period.
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
            type: array
            items:
                $ref: '#/definitions/IMA'
              
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
        result = get_ima_date(data_referencia=data_referencia)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_ima_period(start_date=start_date,end_date=end_date)
        return jsonify(result) , 200
    
    result = IMA.query.all()
    try:
        result = IMASchema().dump(result, many=True)
    except TypeError:
        result = IMASchema().dump(result)
    return jsonify(result),200


@anbima_blueprint.route("/ima/<string:indice>", methods=["GET"])
def get_ima_indice(indice:str):
    """
    Returns all results of an IMA-related index corresponding to the provided id. May be filtered down by date or period.
    ---
    tags:
      - Anbima

    parameters:
      - name: indice
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
                $ref: '#/definitions/IMA'
              
        '400':
          description: Bad Request

        '404':
          description: Bad Request. field `indice` must be a string

    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_ima_date(data_referencia=data_referencia,indice=indice)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_ima_period(start_date=start_date,end_date=end_date,indice=indice)
        return jsonify(result) , 200
    
    result = IMA.query.filter_by(indice=indice).all()
    try:
        result = IMASchema().dump(result, many=True)
    except TypeError:
        result = IMASchema().dump(result)
    return jsonify(result),200




@anbima_blueprint.route("/ima/components/", methods=["GET"])
def get_components():
    """
    Returns the composition of all IMA-related indexes. May be filtered down by date or period.
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
            type: array
            items:
                $ref: '#/definitions/ComponentsIMA'
              
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
        result = get_comp_date(data_referencia=data_referencia)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_comp_period(start_date=start_date,end_date=end_date)
        return jsonify(result) , 200
    
    result = ComponentsIMA.query.all()
    try:
        result = ComponentsIMASchema().dump(result, many=True)
    except TypeError:
        result = ComponentsIMASchema().dump(result)
    return jsonify(result),200


@anbima_blueprint.route("/ima/<string:indice>/components/", methods=["GET"])
def get_components_indice(indice:str):
    """
    Returns the composition of an IMA-related index corresponding to the provided id. May be filtered down by date or period.
    ---
    tags:
      - Anbima
      
    parameters:
      - name: indice
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
                $ref: '#/definitions/ComponentsIMA'
              
        '400':
          description: Bad Request

        '404':
          description: Bad Request. field `indice` must be a string

    """
    args = request.args
    data_referencia = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if data_referencia:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_ima_date(data_referencia=data_referencia,indice=indice)
        return jsonify(result), 200

    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_ima_period(start_date=start_date,end_date=end_date,indice=indice)
        return jsonify(result) , 200

    result = ComponentsIMA.query.filter_by(indice=indice).all()
    try:
        result = ComponentsIMASchema().dump(result, many=True)
    except TypeError:
        result = ComponentsIMASchema().dump(result)
    return jsonify(result),200
