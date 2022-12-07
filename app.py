import logging
import logging.config

from apscheduler import events
from flasgger import Swagger
from flask import Flask
from flask_apscheduler import APScheduler
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pythonjsonlogger import jsonlogger

from api.config import DEFAULT_LOGGER, Config
from api.dbconnection import urls
from api.models.base_model import database
from api.routes.home import example_blueprint
from api.routes.market_index import marketindex_blueprint
from api.routes.sector import sector_blueprint

logging.config.dictConfig(DEFAULT_LOGGER)
logger = logging.getLogger("apscheduler")

""" def event_listener(event):
    if event.exception:
        logger.exception("The job crashed")
    else:
        logger.info("The job ran just fine")

    In create_app we can add the following if we need to
    
    scheduler.add_listener(
        event_listener, events.EVENT_JOB_EXECUTED | events.EVENT_JOB_ERROR
    )


 """


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config())

    app.register_blueprint(example_blueprint)
    app.register_blueprint(sector_blueprint)
    app.register_blueprint(marketindex_blueprint)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    swagger = Swagger(app)
    database.init_app(app)
    return app


# https://auth0.com/blog/best-practices-for-flask-api-development/
# https://github.com/bajcmartinez/flask-api-starter-kit


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
