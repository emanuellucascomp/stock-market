import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_search_stock_response_200(client):
    response = client.get('/search?keywords=IBM')
    assert response.status_code == 200
    assert len(response.get_json().get("bestMatches")) > 0


def test_get_stock_response(client):
    response = client.get('/stock?symbol=IBM')
    assert response.status_code == 200
    assert len(response.get_json().get("Meta Data")) == 5




