import pytest
from app.main import create_app, db
import json
from app.models.plant import Plant
from app.tests.mocked_response import MockedResponse

@pytest.fixture()
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
        session = db.session

        session.add(Plant(name="Plant 1", lat=50.50, long=50.50))
        session.add(Plant(name="Plant 2", lat=60.60, long=60.60))

        session.commit()

    yield app

    with app.app_context():
        db.session.rollback()
        db.drop_all()

@pytest.fixture()
def mocked_weather_api_app(app, mocker):
    with open('app/tests/expected_result.json') as f:    
        response = MockedResponse(json.loads(f.read()), '200')
        mocker.patch('requests.get', return_value=response)

    yield app

