from flask import Blueprint, Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from api.models.base_model import db
from api.config import Config
from flasgger import Swagger

from api.routes.home import example_blueprint
from api.routes.sector import sector_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(example_blueprint)
    app.register_blueprint(sector_blueprint) 
    
    swagger = Swagger(app)
    db.init_app(app)
    return app

# https://auth0.com/blog/best-practices-for-flask-api-development/
# https://github.com/bajcmartinez/flask-api-starter-kit


if __name__ == "__main__":
    app= create_app()
    app.run(debug=True)
