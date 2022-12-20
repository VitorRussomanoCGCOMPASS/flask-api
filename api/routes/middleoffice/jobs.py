import json

from flask import stream_with_context
from flask.wrappers import Response
from flask_apscheduler import api

from api.routes.middleoffice import middleoffice_blueprint


@middleoffice_blueprint.route("/schedule/", methods=["GET"])
def get_scheduler():
    """
    Returns the current schedule of the webapp
    ---

    tags:
        - Middle Office
    
    responses:
        200:
            description: OK

    """
    return api.get_scheduler_info()


@middleoffice_blueprint.route("/jobs/", methods=["GET"])
def get_jobs():
    """
    Returns json with details of all jobs 
    ---

    tags:
        - Middle Office

    responses:
        200:
            description: OK
    """
    return api.get_jobs()


@middleoffice_blueprint.route("/jobs/<string:id>/", methods=["GET"])
def get_job(id: str):
    """
    Returns json with details of the job with the provided ID
    ---

    tags:
        - Middle Office

    responses:
        200:
            description: OK
        404:
            description: Job not found
    """
    return api.get_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/pause/", methods=["POST"])
def pause_job(id: str):
    """
    Pauses a job, returns json of job details

    ---
    tags:
        - Middle Office
    
    responses:
        200:
            description: OK
        404:
            description: Job not found
        500:
            description: Unexpected error
    """    
    return api.pause_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/resume/", methods=["POST"])
def resume_job(id: str):
    """
    Resume a job, returns json of job details

    ---
    tags:
        - Middle Office
    
    responses:
        200:
            description: OK
        404:
            description: Job not found
        500:
            description: Unexpected error
    """    
    return api.resume_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/run/", methods=["POST"])
def run_job(id: str):
    """
    Run a job, returns json of job details

    ---
    tags:
        - Middle Office
    
    responses:
        200:
            description: OK
        404:
            description: Job not found
        500:
            description: Unexpected error
    """    
    return api.run_job(id)


def pause_all_jobs():
    jobs = json.loads(api.get_jobs().data)
    for job in jobs:
        id = job.get("id")
        result = api.pause_job(id)
        yield result.response[0]  # type: ignore


def resume_all_jobs():

    jobs = api.get_jobs().data.decode()

    for job in jobs:
        result = api.resume_job(job.get("id"))
        yield json.dumps(result.response[0])  # type: ignore


@middleoffice_blueprint.route("/jobs/pause/", methods=["POST"])
def streamed_pause_all_jobs():
    """
    Pause all jobs, stream json of jobs details

    ---
    tags:
        - Middle Office
    
    responses:
        200:
            description: OK
        404:
            description: Job not found
        500:
            description: Unexpected error
    """    
    return stream_with_context(Response(pause_all_jobs(), content_type="application/json"))  # type: ignore


@middleoffice_blueprint.route("/jobs/resume/", methods=["POST"])
def streamed_resume_all_jobs():
    """
    Resume all jobs, stream json of jobs details

    ---
    tags:
        - Middle Office
    
    responses:
        200:
            description: OK
        404:
            description: Job not found
        500:
            description: Unexpected error
    """    
    return stream_with_context(Response(resume_all_jobs(), content_type="application/json"))  # type: ignore
