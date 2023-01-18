from flasgger import Swagger
from flasgger import APISpec

from flask import Flask

from flask_api.config import Config

from flask_api.db import database

# from flask_sqlalchemy import SQLAlchemy


from flask_api.routes.currency import currency_blueprint
from flask_api.routes.indexes import indexes_blueprint
from flask_api.routes.market_index import marketindex_blueprint
from flask_api.routes.middleoffice import middleoffice_blueprint
from flask_api.routes.sector import sector_blueprint
from flask_api.routes.anbima import anbima_blueprint
from flask_api.routes.debentures import debentures_blueprint


from apispec.ext.marshmallow import MarshmallowPlugin


from flask_api.schemas.currency import CurrencySchema, CurrencyValuesSchema
from flask_api.schemas.indexes import IndexesSchema, IndexValuesSchema
from flask_api.schemas.holidays import HolidayCalendarsSchema, HolidaysSchema
from flask_api.schemas.sector import SectorEntrySchema, AssetsSectorSchema
from flask_api.schemas.market_index import MarketIndexSchema
from flask_api.schemas.vna import VNASchema
from flask_api.schemas.cricra import CriCraSchema
from flask_api.schemas.ima import IMASchema, ComponentsIMASchema
from flask_api.schemas.debentures import (
    DebenturesSchema,
    OtherDebenturesSchema,
    AnbimaDebenturesSchema,
)


def create_template(app: Flask):
    spec = APISpec(
        title="Compass Brazil API",
        version="1.0",
        openapi_version="2.0",
        plugins=[MarshmallowPlugin()],
    )

    template = spec.to_flasgger(
        app,
        definitions=[
            CurrencySchema,
            CurrencyValuesSchema,
            IndexesSchema,
            IndexValuesSchema,
            HolidayCalendarsSchema,
            HolidaysSchema,
            SectorEntrySchema,
            AssetsSectorSchema,
            MarketIndexSchema,
            VNASchema,
            CriCraSchema,
            ComponentsIMASchema,
            IMASchema,
            DebenturesSchema,
            OtherDebenturesSchema,
            AnbimaDebenturesSchema,
        ],
    )
    return template


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    app.register_blueprint(sector_blueprint)   
    app.register_blueprint(marketindex_blueprint)
    app.register_blueprint(middleoffice_blueprint)
    app.register_blueprint(indexes_blueprint)
    app.register_blueprint(anbima_blueprint)
    app.register_blueprint(debentures_blueprint)
    app.register_blueprint(currency_blueprint)

    template = create_template(app)
    swagger = Swagger(app, template=template)

    database.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app(config_class=Config)

    app.run(debug=True)
