from api.routes.middleoffice import middleoffice_blueprint
from flask import jsonify, request
from api.models.holidays import HolidayCalendars, Holidays
from app import database
from api.schemas.holidays import HolidaysSchema, HolidayCalendarsSchema
from marshmallow import ValidationError


@middleoffice_blueprint.route("/holiday-calendars/", methods=["GET"])
def get_holidaycalendars():
    """
    Returns all Holiday Calendars

    ---

    tags:
        - Middle Office

    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/HolidayCalendars'
    """
    result = HolidayCalendars.query.all()
    result = HolidayCalendarsSchema().dump(result, many=True)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/<int:id>", methods=["GET"])
def get_holidaycalendar_id(id: int):

    """
    Returns the Holiday Calendars associated with the provided ID.


    ---

    tags:
        - Middle Office


    parameters:
      - name: id
        in: path
        type: integer
        required: False

    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/HolidayCalendars'

        '404':
          description: Bad Request. field `id` must be an integer
    """

    result = HolidayCalendars.query.filter_by(id=id).one_or_none()
    result = HolidayCalendarsSchema().dump(result)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/", methods=["POST"])
def post_holidaycalendar():

    """
    Posts a new Holiday Calendar
    ---
    tags:
        - Middle Office

    consumes:
        - application/json

    parameters:
        - in: body
          name: calendar
          description: The calendar to create
          schema:
                $ref: '#/definitions/HolidayCalendars'

    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/HolidayCalendars'

        '400':
            description: Bad Request.
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
        result = HolidayCalendarsSchema(session=database.session).load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    if "id" in request.json:
        id = request.json["id"]
        existing_calendar = HolidayCalendars.query.filter_by(id=id).one_or_none()
        if existing_calendar:
            return (
                jsonify(
                    {
                        "error": "Bad Request",
                        "message": f"Calendar: with id {id} already exists",
                    }
                ),
                400,
            )

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200



@middleoffice_blueprint.route("/holiday-calendars/<int:id>/holidays/", methods=["GET"])
def get_holidays_id(id: int):

    """
    Returns all Holidays associated with a Calendar.
    ---

    tags:
        - Middle Office


    parameters:
      - name: id
        in: path
        type: integer
        required: False

    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/Holidays'
    """

    result = Holidays.query.filter_by(calendar_id=id).all()
    result = HolidaysSchema().dump(result, many=True)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/holidays/", methods=["GET"])
def get_holidays():

    """
    Returns all Holidays associated with a Calendar.
    ---

    tags:
        - Middle Office

    responses:
        200:
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/Holidays'
    """
    result = Holidays.query.all()
    result = HolidaysSchema().dump(result, many=True)
    return jsonify(result), 200


@middleoffice_blueprint.route("/holiday-calendars/holidays/", methods=["POST"])
def post_holidays():
    # TODO: RESPONSES

    """
    Posts a new Holiday
    ---
    tags:
        - Middle Office

    consumes:
        - application/json

    parameters:
        - in: body
          name: holiday
          description: A holiday to create associated with a calendar
          schema:
                $ref: '#/definitions/Holidays'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/Holidays'

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
        result = HolidaysSchema(session=database.session).load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    calendar = request.json["calendar"]["calendar"]

    existing_calendar = HolidayCalendars.query.filter_by(
        calendar=calendar
    ).one_or_none()

    if existing_calendar:
        request.json["calendar"] = HolidayCalendarsSchema().dump(existing_calendar)
        result = HolidaysSchema(session=database.session).load(request.json)

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200
