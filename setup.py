import setuptools

setuptools.setup(
    name="flask_api",
    version="0.1.0",
    url="https://github.com/VitorRussomanoCGCOMPASS/flask_api.git",
    author="VitorRussomanoCGCOMPASS",
    author_email="VitorIbanez@cgcompass.com",
    packages=[
        "flask_api",
        "flask_api.models",
        "flask_api.models.anbima",
        "flask_api.schemas"
    ],
    entry_points = {
        "airflow.plugins" : 
            ["my_plugin = my_plugin:flask_api"]
    }
)
