""" Setup for unittest database access """

from tests.config import TestConfig
from flask import Flask
from flask_testing import TestCase

from api.models.base_model import database as _db
from app import create_app


class BaseTestCase(TestCase):
    def create_app(self) -> Flask:
        app = create_app(TestConfig)
        app_context = app.app_context()
        app_context.push()
        return app

    def setUp(self):

        _db.create_all()

    def tearDown(self):
        _db.session.remove()
        _db.drop_all()
