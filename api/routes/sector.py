from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload
from api.models.sector import AssetsSector, SectorEntry
from api.schemas.sector import AssetsSectorSchema, SectorEntrySchema
from app import database


sector_blueprint = Blueprint("sector", __name__, url_prefix="/sector")

sectorentry_schema = SectorEntrySchema()
assetsector_schema = AssetsSectorSchema()


@sector_blueprint.route("/", methods=["GET"])
def get_sectorentry():
    args = request.args

    methodology = args.get("methodology", type=str)
    if not methodology:
        result = SectorEntry.query.all()
        result = sectorentry_schema.dump(result, many=True)
        return jsonify(result), 200

    result = SectorEntry.query.filter_by(methodology=methodology).all()
    try:
        result = sectorentry_schema.dump(result, many=True)
    except ValueError:
        result = sectorentry_schema.dump(result)
    return jsonify(result), 200


@sector_blueprint.route("/assets/", methods=["POST"])
def create_assetsector():
    data_json = request.get_json()
    if data_json is not None:
        try:
            new_instance = assetsector_schema.loads(data_json)
            database.session.add(new_instance)
            database.session.commit()
            return jsonify(new_instance), 200
        except Exception as err:
            return jsonify({"error": "Bad Request", "message": err}), 400
    return jsonify({"error": "Bad Request", "message": "Empty json data"}), 400


@sector_blueprint.route("/assets/", methods=["GET"])
def get_assetsector():
    args = request.args
    ticker = args.get("ticker", type=str)
    methodology = args.get("methodology", type=str)

    if not args:
        result = AssetsSector.query.options(joinedload(AssetsSector.sector_entry)).all()
        result = assetsector_schema.dump(result, many=True)
        return jsonify(result), 200

    if ticker:
        result = (
            AssetsSector.query.options(joinedload(AssetsSector.sector_entry))
            .filter_by(ticker=ticker)
            .all()
        )
        try:
            result_json = assetsector_schema.dump(result, many=True)
        except ValueError:
            result_json = assetsector_schema.dump(result)
        return jsonify(result_json), 200

    if methodology:
        result = (
            AssetsSector.query.join(AssetsSector.sector_entry, aliased=True)
            .filter_by(methodology=methodology)
            .all()
        )

        try:
            result_json = assetsector_schema.dump(result, many=True)
        except ValueError:
            result_json = assetsector_schema.dump(result)
        return jsonify(result_json), 200

    return jsonify({"error": "Bad Request", "message": "#####"}), 400


""" [docs]class Nested(fields.Nested):

[docs]    def _deserialize(self, *args, **kwargs):
        if hasattr(self.schema, "session"):
            self.schema.session = self.root.session
            self.schema.transient = self.root.transient
        return super()._deserialize(*args, **kwargs) """
