from api.dbconnection import urls
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

DEFAULT_LOGGER = {
    "version": 1,
    "formatters": {
        "formatter_json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s : %(name)s : %(levelname)s : %(module)s.%(funcName)s(%(lineno)d) : %(thread)d %(threadName)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "handler_default": {
            "formatter": "formatter_json",
            "class": "logging.FileHandler",
            "filename": "eventlog.json",
        }
    },
    "loggers": {"root": {"handlers": ["handler_default"], "level": "DEBUG"}},
}


class Config(object):

    """
    App configuration.
    """

    SQLALCHEMY_DATABASE_URI = urls["localdev"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"Title": "API.v1"}
    JOBS = [
        {
            "id": "jobs2",
            "func": "api.events.teste:scheduled_task",
            "trigger": "interval",
            "seconds": 5,
        },
    ]
    SCHEDULER_API_PREFIX = "/middleoffice/scheduler"
    SCHEDULER_API_ENABLED = True
