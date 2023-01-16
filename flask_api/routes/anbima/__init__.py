from flask import Blueprint

anbima_blueprint = Blueprint("Anbima", __name__, url_prefix="/anbima")


from flask_api.routes.anbima import vna, cricra, ima
