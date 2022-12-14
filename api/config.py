from api.dbconnection import urls
import os
import pytz

eventlog_path = os.path.join("api/events/" + "eventslog.json")

DEFAULT_LOGGER = {
    "version": 1,
    "formatters": {
        "formatter_json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "[%(asctime)s : %(name)s : %(levelname)s : %(module)s.%(funcName)s(%(lineno)d) : %(thread)d %(threadName)s: %(message)s]",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "handler_default": {
            "formatter": "formatter_json",
            "class": "logging.FileHandler",
            "filename": eventlog_path,
        }
    },
    "loggers": {"root": {"handlers": ["handler_default"], "level": "DEBUG"}},
}

# ANBIMA 5 PROCESSOS (6:00 AM)
# ( CALENDARIO  )
# B3 CDI 5:00 AM
# BANXICO 5:00 AM
# B3 5:00 AM - D , o resto é d-1
# JGP 9:00 AM

brt = pytz.timezone("America/Sao_Paulo")


class Config(object):

    """
    App configuration.
    """

    SQLALCHEMY_DATABASE_URI = urls["localdev"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"Title": "API.v1"}
    JOBS = [
        {
            "id": "ID1",
            "func": "api.jobs.logevents:upload_logevents",
            "trigger": "cron",
            "day_of_week": "mon-fri",
            "hour":23,
            "minute":59
        },
        {
            "id": "ID2",
            "func": "api.jobs.logevents:upload_logevents",
            "trigger": "cron",
            "day_of_week": "mon-fri",
            "hour":23,
            "minute":59
        }
    ]
    SCHEDULER_TIMEZONE = brt
    SCHEDULER_API_PREFIX = "/middleoffice/scheduler"
    SCHEDULER_API_ENABLED = False
