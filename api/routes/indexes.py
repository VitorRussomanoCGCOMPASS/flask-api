from flask import Blueprint, jsonify, request
from api.models.indexes import Indexes, IndexValues
from api.schemas.indexes import IndexesSchema, IndexValuesSchema


indexes_blueprint = Blueprint("Indexes", __name__, url_prefix="/indexes")

# TODO : CREATE POST METHODS


@indexes_blueprint.route("/", methods=["GET"])
def get_indexes():
    result = Indexes.query.all()
    result = IndexesSchema().dump(result, many=True)
    return jsonify(result), 200


@indexes_blueprint.route("/<int:id>", methods=["GET"])
def get_indexes_id(id: int):
    
    result = Indexes.query.filter_by(id=id).one_or_404()
    result = IndexesSchema().dump(result)
    return jsonify(result), 200


@indexes_blueprint.route("/values/", methods=["GET"])
def get_indexes_values():
    
    result = IndexValues.query.all()
    result = IndexValuesSchema().dump(result, many=True)
    return jsonify(result), 200


@indexes_blueprint.route("/<int:id>/values/", methods=["GET"])
def get_indexes_values_id(id: int):
    
    result = IndexValues.query.filter_by(index_id=id).all()
    result = IndexValuesSchema().dump(result, many=True)
    return jsonify(result), 200


