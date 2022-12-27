import datetime
import json

from flask import jsonify, request

from api.models.eventlog import EventLog
from api.request_schemas.dateargs import DateSchema, PeriodSchema
from api.routes.middleoffice import middleoffice_blueprint
from api.schemas.eventlog import EventLogSchema


def get_eventlog_period(start_date, end_date):
    """

    Get event log between period

    Parameters
    ----------
    start_date : str
        "%Y-%m-%d" format
    end_date : str
        "%Y-%m-%d" format

    """
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")  # type: ignore (Already marshmallow validated)
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")  # type: ignore (Already marshmallow validated)
    start_date_start = start_date.replace(hour=0, minute=0, second=0)
    end_date_end = end_date.replace(hour=23, minute=59, second=59)
    result = EventLog.query.filter(
        EventLog.asctime.between(start_date_start, end_date_end)
    ).all()
    result = EventLogSchema().dump(result, many=True)
    return result


def get_eventlog_date(asctime):

    asctime = datetime.datetime.strptime(asctime, "%Y-%m-%d")
    asctime_start = asctime.replace(hour=0, minute=0, second=0)
    asctime_end = asctime.replace(hour=23, minute=59, second=59)
    result = EventLog.query.filter(
        EventLog.asctime.between(asctime_start, asctime_end)
    ).all()
    result = EventLogSchema().dump(result, many=True)
    return result


@middleoffice_blueprint.route("/event-logs/current/", methods=["GET"])
def get_currenteventlogs():

    """
    Returns all current Event-logs

    ---

    tags:
        - Middle Office


    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/EventLog'

    """

    eventlogs = []
    with open("api/jobs/eventslog.json",mode='r') as file:
        for line in file:
            eventlogs.append(json.loads(line))
    return jsonify(eventlogs), 200


@middleoffice_blueprint.route("/event-logs/", methods=["GET"])
def get_eventlogs():
    """
    Returns non-current Event-Logs. Which may be filtered down by date or period.
    ---
    
    tags:
        - Middle Office

    parameters:
      - name: date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The date of the event-logs to filter by.
            This parameter is incompatible with `start_date`, `end_date`.


      - name: start_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The start_date for the period of which the event-logs will be filtered. Must be used together with `end_date`.
            This parameter is incompatible with `date`.

      - name: end_date
        in: query
        type: string
        required: False
        format: 'YYYY-mm-dd'
        description:
            The end_date for the period of which the event-logs will be filtered. Must be used together with `start_date`.
            This parameter is incompatible with `date`.

    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/EventLog'
              
        '400':
          description: Bad Request




    """

    args = request.args
    asctime = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if asctime:
        errors = DateSchema().validate(args)
        if errors:
            return jsonify({"error": "Bad Request", "message": errors}), 400

        result = get_eventlog_date(asctime)
        return jsonify(result), 200

    if end_date or start_date:
        errors = PeriodSchema().validate(args)
        if errors:
            return jsonify({"error": "Bad Request", "message": errors}), 400

        result = get_eventlog_period(start_date, end_date)
        return jsonify(result), 200

    result = EventLog.query.all()
    result = EventLogSchema().dump(result, many=True)
    return jsonify(result), 200
