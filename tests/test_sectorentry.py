from tests.base import BaseTestCase
from api.models.sector import SectorEntry
from api.models.base_model import database as _db

class SomeTest(BaseTestCase):
    def test_something(self):

        sectorentry = SectorEntry(methodology="Test", sector="Test", subsector=1)
        _db.session.add(sectorentry)
        _db.session.commit()

        assert sectorentry in _db.session
