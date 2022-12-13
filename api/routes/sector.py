from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload

from api.models.sector import AssetsSector, SectorEntry
from api.schemas.sector import AssetsSectorSchema, SectorEntrySchema
from app import database
from api.request_schemas.sector import SectorQuerySchema, AssetSectorQuerySchema


sector_blueprint = Blueprint("sector", __name__, url_prefix="/sectors")

sectorentry_schema = SectorEntrySchema()
assetsector_schema = AssetsSectorSchema()


@sector_blueprint.route("/", methods=["GET"])
def get_sectorentry():
    args = request.args
    methodology = args.get("methodology", type=str)

    if methodology:
        error = SectorQuerySchema().validate(args)

        if error:
            return jsonify({"error": "Bad request", "message": error}), 400
        result = SectorEntry.query.filter_by(**args).all()
        result = sectorentry_schema.dump(result, many=True)
        return jsonify(result), 200

    result = SectorEntry.query.all()
    result = sectorentry_schema.dump(result, many=True)
    return jsonify(result), 200


@sector_blueprint.route("/assets/", methods=["GET"])
def get_assetsector():
    args = request.args

    if args:
        error = AssetSectorQuerySchema().validate(args)
        if error:
            return jsonify({"error": "Bad request", "message": error}) ,400

        result = (
            AssetsSector.query.join(AssetsSector.sector_entry, aliased=True)
            .filter_by(**args)
            .all()
        )

        try:
            result_json = assetsector_schema.dump(result, many=True)
        except ValueError:
            result_json = assetsector_schema.dump(result)
        return jsonify(result_json), 200

    result = AssetsSector.query.options(joinedload(AssetsSector.sector_entry)).all()
    result = assetsector_schema.dump(result, many=True)
    return jsonify(result), 200


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
