import pytest
from backend import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
