import pytest

from sensors_backend import create_app

@pytest.fixture()
def app():
    # set up
    app = create_app({
        'TESTING': True
    })

    yield app

    # tear down

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
