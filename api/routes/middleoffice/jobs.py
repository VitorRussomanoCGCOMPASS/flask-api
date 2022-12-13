from flask import jsonify, request
from flask_apscheduler import api

from api.request_schemas.jobs import JobsQuerySchema
from api.routes.middleoffice import middleoffice_blueprint


@middleoffice_blueprint.route("/schedule/", methods=["GET"])
def get_scheduler():
    return api.get_scheduler_info()


@middleoffice_blueprint.route("/jobs/", methods=["GET"])
def get_jobs():
    args = request.args
    id = args.get("id", type=str)
    if args:
        error = JobsQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad Request", "message": error}), 400
        return api.get_job(id)

    return api.get_jobs(), 200


@middleoffice_blueprint.route("/jobs/pause/", methods=["POST"])
def pause_job():
    args = request.args
    id = args.get("id", type=str)
    error = JobsQuerySchema().validate(args)
    if error:
        return jsonify({"error": "Bad Request", "message": error}), 400
    return api.pause_job(id), 200


@middleoffice_blueprint.route("/jobs/resume/", methods=["POST"])
def resume_job():
    args = request.args
    id = args.get("id", type=str)
    error = JobsQuerySchema().validate(args)
    if error:
        return jsonify({"error": "Bad Request", "message": error}), 400
    return api.resume_job(id), 200


@middleoffice_blueprint.route("/jobs/run/", methods=["POST"])
def run_job():
    args = request.args
    id = args.get("id", type=str)
    error = JobsQuerySchema().validate(args)
    if error:
        return jsonify({"error": "Bad Request", "message": error}), 400
    return api.run_job(id), 200
