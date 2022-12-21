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
       '200':
             description: OK
             schema:
               type: object
               properties:
                     current_host:
                       type: string
                     allowed_hosts:
                       type: string
                     running:
                       type: boolean
    """
    return api.get_scheduler_info()


@middleoffice_blueprint.route("/jobs/", methods=["GET"])
def get_all_jobs():
    """
    Returns the current schedule of the webapp
    ---

    tags:
            - Middle Office


    responses:
       '200':
             description: OK
             schema:
               type: array
               items:
                 properties:
                       id:
                         type: string
                       name:
                         type: string
                       func:
                         type: string
                       args:
                         type: object
                       kwargs:
                         type: object
                       trigger:
                         type: string
                       day_of_week:
                         type: string
                       hour:
                         type: string
                       minute:
                         type: string
                       misfire_grace_time:
                         type: integer
                       max_instances:
                         type: integer
                       next_run_time:
                         type: string

    """
    return api.get_jobs()


@middleoffice_blueprint.route("/jobs/<string:id>/", methods=["GET"])
def get_job(id: str):
    """
    Returns json with details of the job with the provided id
    ---

    tags:
            - Middle Office


    responses:
       '200':
             description: OK
             schema:
               type: object
               properties:
                     id:
                       type: string
                     name:
                       type: string
                     func:
                       type: string
                     args:
                       type: object
                     kwargs:
                       type: object
                     trigger:
                       type: string
                     day_of_week:
                       type: string
                     hour:
                       type: string
                     minute:
                       type: string
                     misfire_grace_time:
                       type: integer
                     max_instances:
                       type: integer
                     next_run_time:
                       type: string

       '404':
             description: Job not found
    """
    return api.get_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/pause/", methods=["POST"])
def pause_job(id: str):
    """
    Pauses a job and returns json of job details
    ---

    tags:
            - Middle Office


    responses:
       '200':
             description: OK
             schema:
               type: object
               properties:
                     id:
                       type: string
                     name:
                       type: string
                     func:
                       type: string
                     args:
                       type: object
                     kwargs:
                       type: object
                     trigger:
                       type: string
                     day_of_week:
                       type: string
                     hour:
                       type: string
                     minute:
                       type: string
                     misfire_grace_time:
                       type: integer
                     max_instances:
                       type: integer
                     next_run_time:
                       type: string

       '404':
             description: Job not found

       '500':
             description: Unexpected error
    """
    return api.pause_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/resume/", methods=["POST"])
def resume_job(id: str):
    """
    Resume a job and returns json of job details
    ---

    tags:
            - Middle Office


    responses:
       '200':
             description: OK
             schema:
               type: object
               properties:
                     id:
                       type: string
                     name:
                       type: string
                     func:
                       type: string
                     args:
                       type: object
                     kwargs:
                       type: object
                     trigger:
                       type: string
                     day_of_week:
                       type: string
                     hour:
                       type: string
                     minute:
                       type: string
                     misfire_grace_time:
                       type: integer
                     max_instances:
                       type: integer
                     next_run_time:
                       type: string

       '404':
             description: Job not found

       '500':
             description: Unexpected error

    """
    return api.resume_job(id)


@middleoffice_blueprint.route("/jobs/<string:id>/run/", methods=["POST"])
def run_job(id: str):
    """
    Run a job and returns json of job details
    ---

    tags:
            - Middle Office


    responses:
       '200':
             description: OK
             schema:
               type: object
               properties:
                     id:
                       type: string
                     name:
                       type: string
                     func:
                       type: string
                     args:
                       type: object
                     kwargs:
                       type: object
                     trigger:
                       type: string
                     day_of_week:
                       type: string
                     hour:
                       type: string
                     minute:
                       type: string
                     misfire_grace_time:
                       type: integer
                     max_instances:
                       type: integer
                     next_run_time:
                       type: string

       '404':
             description: Job not found

       '500':
             description: Unexpected error

    """
    return api.run_job(id)


""" 
responses:
    '200':
      description: An array of videos
      schema:
        type: array
        items:
          $ref: '#/definitions/Video' 
 """
