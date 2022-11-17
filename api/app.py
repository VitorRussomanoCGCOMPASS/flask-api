from flask import Blueprint, Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.models import SectorEntry


class SectorEntrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SectorEntry


sector_entry_schema = SectorEntrySchema()

home_api = Blueprint('api',__name__)

@home_api.route('/')
def welcome():
    return {"message": "Home"}, 200


@app.route("/SectorEntry/",methods=['GET'])
def sector_entry_list():
    all_entries = SectorEntry.query.all()
    return jsonify(sector_entry_schema.dump(all_entries, many=True))


@app.route("/SectorEntry/", methods=["POST"])
def create_sector_entry():

    if request.is_json:
        data = request.get_json()

        sectorentry = SectorEntry(
            methodology=data["methodology"],
            sector=data["sector"],
            subsector=data["subsector"],
        )

        db.session.add(sectorentry)
        db.session.commit()
    
        return make_response("Sucess", 200)
    else:
        return make_response("Being Called", 400)


# https://auth0.com/blog/best-practices-for-flask-api-development/
# https://github.com/bajcmartinez/flask-api-starter-kit


if __name__ == "__main__":
    app.run(debug=True)
