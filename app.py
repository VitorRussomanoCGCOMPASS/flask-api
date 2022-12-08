import logging
import logging.config

from flasgger import Swagger
from flask import Flask
from flask_apscheduler import APScheduler

from api.config import DEFAULT_LOGGER, Config
from api.models.base_model import database
from api.routes.eventlog import middleoffice_blueprint
from api.routes.home import example_blueprint
from api.routes.market_index import marketindex_blueprint
from api.routes.sector import sector_blueprint

# logging.config.dictConfig(DEFAULT_LOGGER)
# logger = logging.getLogger("apscheduler")


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config())

    app.register_blueprint(example_blueprint)
    app.register_blueprint(sector_blueprint)
    app.register_blueprint(marketindex_blueprint)
    app.register_blueprint(middleoffice_blueprint)

    
    #scheduler = APScheduler()
    #scheduler.init_app(app)
    #scheduler.start()

    swagger = Swagger(app)
    database.init_app(app)
    return app


# https://auth0.com/blog/best-practices-for-flask-api-development/
# https://github.com/bajcmartinez/flask-api-starter-kit


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
