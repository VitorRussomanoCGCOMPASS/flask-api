from flask import Blueprint, jsonify, request
from api.models.indexes import Indexes, IndexValues
from api.schemas.indexes import IndexesSchema, IndexValuesSchema
from marshmallow import ValidationError
from app import database
from api.request_schemas.dateargs import DateSchema, PeriodSchema

indexes_blueprint = Blueprint("Indexes", __name__, url_prefix="/indexes")

# TODO : CREATE POST METHODS


@indexes_blueprint.route("/", methods=["GET"])
def get_indexes():
    """
    Returns all Indexes
    ---


    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/Indexes'
              

    """
    result = Indexes.query.all()
    try:
        result = IndexesSchema().dump(result, many=True)
    except TypeError:
        result = IndexesSchema().dump(result)
    return jsonify(result), 200


@indexes_blueprint.route("/<int:id>", methods=["GET"])
def get_indexes_id(id: int):
    """
    Returns the Indexes associated with the provided id
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
                $ref: '#/definitions/Indexes'

        '404':
          description: Bad Request. field `id` must be an integer 
    
    """
    result = Indexes.query.filter_by(id=id).one()
    result = IndexesSchema().dump(result)
    return jsonify(result), 200


def get_index_period(start_date, end_date, index_id):
    if index_id:
        result = (
            IndexValues.query.filter(IndexValues.date.between(start_date, end_date))
            .filter_by(index_id=index_id)
            .all()
        )
    else:
        result = IndexValues.query.filter(
            IndexValues.date.between(start_date, end_date)
        ).all()
    try:
        result = IndexValuesSchema().dump(result, many=True)
    except TypeError:
        result = IndexValuesSchema().dump(result)
    return result


def get_index_date(date, index_id):

    if index_id:
        result = IndexValues.query.filter_by(
            index_id=index_id, date=date
        ).first_or_404()

    else:
        result = IndexValues.query.filter_by(date=date).all()

    try:
        result = IndexValuesSchema().dump(result, many=True)
    except TypeError:
        result = IndexValuesSchema().dump(result)
    return result


@indexes_blueprint.route("/values/", methods=["GET"])
def get_indexes_values():
    """
    Returns all values associated with all Indexes. May be filtered down by date or period.

    ---
    parameters:
      - name: date
        in: query
        type: string
        required: False
        format:  'YYYY-mm-dd'
        description:
            This parameter is incompatible with `start_date` and `end_date`.


      - name: start_date
        in: query
        type: string
        required: False
        format:  'YYYY-mm-dd'
        description:
            The start_date for the period of which the values will be filtered. Must be used together with `end_date`.
            This parameter is incompatible with `date`.

      - name: end_date
        in: query
        type: string
        required: False
        format:  'YYYY-mm-dd'
        description:
            The end_date for the period of which the values will be filtered. Must be used together with `start_date`.
            This parameter is incompatible with `date`.

    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/IndexValues'

        '400':
          description: Bad Request.

    """
    args = request.args
    date = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if date:
        error = DateSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_index_date(date=date, index_id=None)
        return jsonify(result), 200
    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_index_period(start_date, end_date, index_id=None)
        return jsonify(result), 200

    result = IndexValues.query.all()
    try:
        result = IndexValuesSchema().dump(result, many=True)
    except TypeError:
        result = IndexValuesSchema().dump(result)
    return jsonify(result), 200


@indexes_blueprint.route("/<int:id>/values/", methods=["GET"])
def get_indexes_values_id(id: int):
    """
    Returns all values associated with a Index. May be filtered down by date or period.
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
        format:  'YYYY-mm-dd'
        description:
            The start_date for the period of which the values will be filtered. Must be used together with `end_date`.
            This parameter is incompatible with `date`.

      - name: end_date
        in: query
        type: string
        required: False
        format:  'YYYY-mm-dd'
        description:
            The end_date for the period of which the values will be filtered. Must be used together with `start_date`.
            This parameter is incompatible with `date`.

    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/IndexValues'

        '400':
          description: Bad Request.
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
        result = get_index_date(date=date, index_id=id)
        return jsonify(result), 200
    if start_date or end_date:
        error = PeriodSchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        result = get_index_period(start_date, end_date, index_id=id)
        return jsonify(result), 200

    result = IndexValues.query.filter_by(index_id=id).all()
    try:
        result = IndexValuesSchema().dump(result, many=True)
    except TypeError:
        result = IndexValuesSchema().dump(result)
    return jsonify(result), 200


@indexes_blueprint.route("/", methods=["POST"])
def post_index():

    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:
        try:
            result = IndexesSchema().load(request.json)
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


@indexes_blueprint.route("/values/", methods=["POST"])
def post_indexes_values():
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:
        try:
            result = IndexValuesSchema().load(request.json)
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
    