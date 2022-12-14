from api.routes.middleoffice import middleoffice_blueprint
from flask import jsonify, request
from api.models.holidays import HolidayCalendars, Holidays
from app import database
from api.schemas.holidays import HolidaysSchema, HolidayCalendarsSchema
from api.request_schemas.holidays import HolidaysQuerySchema
from marshmallow import ValidationError


@middleoffice_blueprint.route("/holiday-calendars/", methods=["GET"])
def get_holidaycalendars():
    result = HolidayCalendars.query.all()
    try:
        result = HolidayCalendarsSchema().dump(result, many=True)
    except ValueError:
        result = HolidayCalendarsSchema().dump(result)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/", methods=["POST"])
def post_holidaycalendar():
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:
        try:
            result = HolidayCalendarsSchema().load(request.json)
        except ValidationError as err:
            return jsonify({"error": "Bad Request", "message": err.messages}), 400

        try:
            database.session.add(result)
            database.session.commit()
            return jsonify(request.json), 200
        except Exception as exc:
            return (
                jsonify({"error": "Server Unavailable", "message": "######"}),
                400,
            )

    return jsonify({"error": "Bad Request", "message": "empty json"}), 400


@middleoffice_blueprint.route("/holidays/", methods=["GET"])
def get_holidays():
    args = request.args
    id = args.get("id", type=int)

    if args:
        error = HolidaysQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad request", "message": error}), 400

        args = HolidaysQuerySchema().load(args)
        result = Holidays.query.filter_by(**args).all()
        result = HolidaysSchema().dump(result, many=True)
        return jsonify(result), 200

    result = Holidays.query.all()
    result = HolidaysSchema().dump(result, many=True)
    return jsonify(result), 200



@middleoffice_blueprint.route("/holidays/", methods=["POST"])
def post_holidays():
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:
        try:
            result = HolidaysSchema().load(request.json)
        except ValidationError as err:
            return jsonify({"error": "Bad Request", "message": err.messages}), 400

        try:
            database.session.add(result)
            database.session.commit()
            return jsonify(request.json), 200
        except Exception as exc:
            return (
                jsonify({"error": "Server Unavailable", "message": "######"}),
                400,
            )

    return jsonify({"error": "Bad Request", "message": "empty json"}), 400
