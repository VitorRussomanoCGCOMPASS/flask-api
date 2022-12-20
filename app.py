import logging
import logging.config

from flasgger import Swagger
from flasgger import APISpec

from flask import Flask
from flask_apscheduler import APScheduler

from api.config import DEFAULT_LOGGER, Config
from api.models.base_model import database
from api.routes.currency import currency_blueprint
from api.routes.indexes import indexes_blueprint
from api.routes.market_index import marketindex_blueprint
from api.routes.middleoffice import middleoffice_blueprint
from api.routes.sector import sector_blueprint


from apispec.ext.marshmallow import MarshmallowPlugin

# logging.config.dictConfig(DEFAULT_LOGGER)
# logger = logging.getLogger("apscheduler")

spec = APISpec("My api docs", "1.0", "2.0", plugins=[MarshmallowPlugin()])


from api.schemas.currency import CurrencySchema, CurrencyValuesSchema
from api.schemas.indexes import IndexesSchema, IndexValuesSchema


def create_template(app: Flask):
    template = spec.to_flasgger(
        app,
        definitions=[
            CurrencySchema,
            CurrencyValuesSchema,
        ],
    )
    return template


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(sector_blueprint)
    app.register_blueprint(marketindex_blueprint)
    app.register_blueprint(middleoffice_blueprint)
    app.register_blueprint(currency_blueprint)
    app.register_blueprint(indexes_blueprint)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    template = create_template(app)
    swagger = Swagger(app, template=template)
    database.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app(config_class=Config)
    app.run(debug=True)
