from api.dbconnection import urls

class Config(object):

    """App configuration."""

    SQLALCHEMY_DATABASE_URI = urls["localdev"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"Title": "API.v1"}
    JOBS = [
        {
            "id": "job1",
            "func": "api.events.teste:scheduled_task",
            "trigger": "interval",
            "seconds": 5,
        }
    ]

    SCHEDULER_API_ENABLED = True