from flask import Blueprint

anbima_blueprint = Blueprint("Anbima", __name__, url_prefix="/anbima")


from api.routes.anbima import vna, crica, ima
