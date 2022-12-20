from api.routes.middleoffice import middleoffice_blueprint
from flask import jsonify, request
from api.models.holidays import HolidayCalendars, Holidays
from app import database
from api.schemas.holidays import HolidaysSchema, HolidayCalendarsSchema
from marshmallow import ValidationError

# TODO : REVIEW POST METHODS

@middleoffice_blueprint.route("/holiday-calendars/", methods=["GET"])
def get_holidaycalendars():
    result = HolidayCalendars.query.all()
    try:
        result = HolidayCalendarsSchema().dump(result, many=True)
    except TypeError:
        result = HolidayCalendarsSchema().dump(result)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/<int:id>", methods=["GET"])
def get_holidaycalendar_id(id: int):
    result = HolidayCalendars.query.filter_by(id=id).one_or_404()
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


@middleoffice_blueprint.route("/holiday-calendars/<int:id>/holidays/", methods=["GET"])
def get_holidays_id(id: int):
    result = Holidays.query.filter_by(calendar_id=id).all()
    result = HolidaysSchema().dump(result, many=True)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/holidays/", methods=["GET"])
def get_holidays():
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
