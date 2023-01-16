from flask_api.models.sector import SectorEntry
from pytest import fixture


@fixture(scope='module')
def new_sectorentry():
    sectorentry_dbo = SectorEntry(methodology='SARAIVA',sector='sectorA',subsector='subsectorA')
    
def test_get_sectorentry(session,new_sectorentry):





def test_config(app):
    assert app.testing == True


def test_post_model(session):
    sectorentry = SectorEntry(methodology="Test", sector="Test", subsector=1)
    session.add(sectorentry)
    session.commit()

    assert sectorentry.sector == "Test"
