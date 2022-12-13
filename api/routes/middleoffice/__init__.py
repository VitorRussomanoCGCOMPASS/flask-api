from flask import Blueprint

middleoffice_blueprint = Blueprint("Middleoffice", __name__, url_prefix="/middleoffice")


@middleoffice_blueprint.route('/',methods=['GET'])
def middle_office_home():
    return "Middle office route"


from api.routes.middleoffice import eventlog, jobs
