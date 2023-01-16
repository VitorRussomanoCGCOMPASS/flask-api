from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload

from flask_api.models.sector import AssetsSector, SectorEntry
from flask_api.schemas.sector import AssetsSectorSchema, SectorEntrySchema
from flask_api.app import database


sector_blueprint = Blueprint("sector", __name__, url_prefix="/sectors")


@sector_blueprint.route("/", methods=["GET"])
def get_sectorentry():
    """
    Returns all methodologies with their respectives sector and subsectors classification
    ---



    responses:
        '200':
          description: OK
          schema:
            type: array
            items:
                $ref: '#/definitions/SectorEntry'
    """
    result = SectorEntry.query.all()
    result = SectorEntrySchema().dump(result, many=True)
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
    result = SectorEntrySchema().dump(result, many=True)
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
            type: array
            items:
                $ref: '#/definitions/AssetsSector'
    """

    result = AssetsSector.query.options(joinedload(AssetsSector.sector_entry)).all()
    result = AssetsSectorSchema().dump(result, many=True)
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
            type: array
            items:
                $ref: '#/definitions/AssetsSector'
        '404':
          description: Bad Request. field `Methodology` must be a string.

    """

    result = (
        AssetsSector.query.join(AssetsSector.sector_entry, aliased=True)
        .filter_by(methodology=methodology)
        .all()
    )
    result_json = AssetsSectorSchema().dump(result, many=True)
    return jsonify(result_json), 200


@sector_blueprint.route("/", methods=["POST"])
def create_sectorentry():
    """
    Create a new sector entry
    ---


    consumes:
        - application/json

    parameters:
        - in: body
          name: sector 
          description: The new sector classification to create
          schema:
                $ref: '#/definitions/SectorEntry'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/SectorEntry'

        '400':
            description: Bad Request
    """    
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )

    if not request.json:
        return (jsonify({"error": "Bad Request", "message": "Empty data"}), 400)

    try:
        result = SectorEntrySchema().load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200


@sector_blueprint.route("/assets/", methods=["POST"])
def create_assetsector():
    """
    Registry a asset to a sector classification
    ---

    consumes:
        - application/json

    parameters:
        - in: body
          name: asset sector classification
          description: The asset along with the sector classification 
          schema:
                $ref: '#/definitions/AssetsSector'
    responses:
        '200':
            description: OK
            schema:
                type: object
                $ref : '#/definitions/AssetsSector'

        '400':
            description: Bad Request
    """
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return (
            jsonify({"error": "Bad Request", "message": "Content-Type not supported"}),
            400,
        )

    if not request.json:
        return (jsonify({"error": "Bad Request", "message": "Empty data"}), 400)

    try:
        result = AssetsSectorSchema(database.session).load(request.json)
    except ValidationError as err:
        return jsonify({"error": "Bad Request", "message": err.messages}), 400
    sector_entry = request.json["sector_entry"]

    existing_sectorentry = SectorEntry.query.filter_by(**sector_entry).one_or_none()
    if existing_sectorentry:
        request.json["sector_entry"] = SectorEntrySchema().dump(existing_sectorentry)
        result = AssetsSectorSchema(session=database.session).load(request.json)

    database.session.add(result)
    database.session.commit()
    return jsonify(request.json), 200
