from api.routes.middleoffice import middleoffice_blueprint
from flask import jsonify, request
from api.models.holidays import HolidayCalendars, Holidays
from app import database
from api.schemas.holidays import HolidaysSchema, HolidayCalendarsSchema
from marshmallow import ValidationError

# TODO : REVIEW POST METHODS

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
    try:
        result = HolidayCalendarsSchema().dump(result, many=True)
    except TypeError:
        result = HolidayCalendarsSchema().dump(result)
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
   
   
   
   
    result = HolidayCalendars.query.filter_by(id=id).one()
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
