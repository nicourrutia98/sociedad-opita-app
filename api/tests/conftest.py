"""
pytest fixtures para tests de la API.

Usa moto para mockear AWS services (DynamoDB, API Gateway, Lambda).
Para S1: solo necesitamos el cliente de test de FastAPI (TestClient).
"""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """TestClient de FastAPI para tests sin levantar servidor real."""
    from api.main import app
    return TestClient(app)


@pytest.fixture
def aws_credentials(monkeypatch):
    """Mock AWS credentials para moto."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
