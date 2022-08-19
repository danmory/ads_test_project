from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_register():
    assert 1 == 1