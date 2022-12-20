from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload

from api.models.sector import AssetsSector, SectorEntry
from api.schemas.sector import AssetsSectorSchema, SectorEntrySchema
from app import database


sector_blueprint = Blueprint("sector", __name__, url_prefix="/sectors")

sectorentry_schema = SectorEntrySchema()
assetsector_schema = AssetsSectorSchema()


@sector_blueprint.route("/", methods=["GET"])
def get_sectorentry():
    """
    Returns all methodologies with their respectives sector and subsectors classification
    ---


        
    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/SectorEntry'
    """
    result = SectorEntry.query.all()
    result = sectorentry_schema.dump(result, many=True)
    return jsonify(result), 200


@sector_blueprint.route("/<string:methodology>", methods=["GET"])
def get_sector_entry_methodology(methodology: str):

    """
    Returns all sectors and subsectors associated with a methodology
    ---

    parameters:
      - name: methodology
        in: path
        type: integer
        required: False


        
    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/SectorEntry'

    """
    result = SectorEntry.query.filter_by(methodology=methodology).all()
    result = sectorentry_schema.dump(result, many=True)
    return jsonify(result), 200


@sector_blueprint.route("/assets/", methods=["GET"])
def get_assetsector():
    """
    Returns all assets and their sectors and subsectors classification
    ---

        
    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/AssetsSector'
    """

    result = AssetsSector.query.options(joinedload(AssetsSector.sector_entry)).all()
    result = assetsector_schema.dump(result, many=True)
    return jsonify(result), 200


@sector_blueprint.route("/<string:methodology>/assets/", methods=["GET"])
def get_assetsector_methodology(methodology: str):

    """
    Returns all assets and their sectors and subsectors classification associated with a methodology
    ---

    parameters:
      - name: methodology
        in: path
        type: integer
        required: False


         
    responses:
        '200':
          description: OK
          schema:
                $ref: '#/definitions/AssetsSector'
        '404':
          description: Bad Request. field `Methodology` must be a string.

    """

    result = (
        AssetsSector.query.join(AssetsSector.sector_entry, aliased=True)
        .filter_by(methodology=methodology)
        .all()
    )
    try:
        result_json = assetsector_schema.dump(result, many=True)
    except TypeError:
        result_json = assetsector_schema.dump(result)
    return jsonify(result_json), 200


@sector_blueprint.route("/assets/", methods=["POST"])
def create_assetsector():
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )
    if request.json:

        try:
            result = assetsector_schema.load(request.json)
        except ValidationError as err:
            return jsonify({"error": "Bad Request", "message": err.messages}), 400
        try:
            database.session.add(result)
            database.session.commit()
        except Exception as exc:
            return (
                jsonify({"error": "Server Unavailable", "message": "######"}),
                400,
            )
    return jsonify(request.json), 200
