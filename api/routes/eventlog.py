from flask import Blueprint, jsonify, request
from api.models.eventlog import EventLog
from api.schemas.eventlog import EventLogSchema
from sqlalchemy.orm import Query
import datetime
from api.request_schemas.dateargs import DateargsSchema

eventlog_schema = EventLogSchema()
middleoffice_blueprint = Blueprint("Middleoffice", __name__, url_prefix="/middleoffice")


def get_eventlog_today():

    today = datetime.datetime.today()
    today_start = today.replace(hour=0, minute=0, second=0)
    today_end = today.replace(hour=23, minute=59, second=59)
    result = EventLog.query.filter(
        EventLog.asctime.between(today_start, today_end)
    ).all()
    result = eventlog_schema.dump(result, many=True)
    return result


def get_eventlog_period(start_date,end_date):
    
    start_date = datetime.datetime.strptime(start_date,"%Y-%m-%d") # type: ignore (Already marshmallow validated)
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d") # type: ignore (Already marshmallow validated)
    start_date_start = start_date.replace(hour=0,minute=0,second=0)
    end_date_end = end_date.replace(hour=23,minute=59,second=59)
    result= EventLog.query.filter(EventLog.asctime.between(start_date_start,end_date_end)).all()
    result = eventlog_schema.dump(result,many=True)
    return result

 
@middleoffice_blueprint.route("/eventlogs/")
def get_eventlog_date():
    args = request.args
    asctime = args.get("date", type=str)
    start_date = args.get("start_date", type=str)
    end_date = args.get("end_date", type=str)

    if asctime:
        asctime = datetime.datetime.strptime(asctime, "%Y-%m-%d")

        asctime_start = asctime.replace(hour=0, minute=0, second=0)
        asctime_end = asctime.replace(hour=23, minute=59, second=59)
        result = EventLog.query.filter(
            EventLog.asctime.between(asctime_start, asctime_end)
        ).all()
        result = eventlog_schema.dump(result, many=True)
        return jsonify(result), 200
  
  
    if end_date or start_date:
        errors = DateargsSchema().validate(args)
        if errors:
            return jsonify({"error": "Bad Request", "message": errors}), 400

        result =get_eventlog_period(start_date,end_date)
        return  jsonify(result) , 200 
   
   
    result = get_eventlog_today()
    return jsonify(result), 200

       