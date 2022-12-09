from api.models.sector import SectorEntry


def test_config(app):
    assert app.testing == True


def test_post_model(session):
    sectorentry = SectorEntry(methodology="Test", sector="Test", subsector=1)
    session.add(sectorentry)
    session.commit()

    assert sectorentry.sector == "Test"
