from tests.unit.base import BaseTestCase
from api.models.sector import SectorEntry
from api.models.base_model import database as _db



class SomeTest(BaseTestCase):

    def test_something(self):

        sectorentry= SectorEntry(methodology= 'Test',sector='Test',subsector=1)
        _db.session.add(sectorentry)
        _db.session.commit()
        print(sectorentry.subsector)
        # this works
        assert sectorentry in _db.session



def test_post_model(session):
    sectorentry= SectorEntry(methodology= 'Test',sector='Test',subsector=1)
    session.add(sectorentry)
    session.commit()

    assert sectorentry.sector == 'Test'