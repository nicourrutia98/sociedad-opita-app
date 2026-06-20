"""
Smoke tests para POST /v1/simulate.

S1: el endpoint retorna placeholder honesto (sin llamada real a LLM).
S2: se mockea DeepSeek con httpx mock o moto.
"""

from fastapi.testclient import TestClient


def test_simulate_s1_placeholder(client: TestClient):
    """POST /v1/simulate retorna placeholder honesto en S1."""
    response = client.post(
        "/v1/simulate",
        json={
            "city_id": "tello",
            "persona_id": "dona_rosa_tendera",
            "scene": {"time": "08:00", "place": "Tienda Dona Rosa"},
            "model": "deepseek-chat",
            "temperature": 1.3,
        },
    )

    assert response.status_code == 200
    body = response.json()

    # En S1 el texto es placeholder
    assert "no disponible" in body["text"].lower()
    assert "deepseek" in body["text"].lower() or "backend" in body["text"].lower()

    # Metadata consistente
    meta = body["metadata"]
    assert meta["model"] == "deepseek-chat"
    assert meta["temperature"] == 1.3
    assert meta["cost_usd"] == 0.0
    assert meta["latency_ms"] == 0


def test_simulate_ciudad_inexistente(client: TestClient):
    """POST /v1/simulate con city_id inexistente retorna 404."""
    response = client.post(
        "/v1/simulate",
        json={
            "city_id": "inexistente",
            "persona_id": "don_rosalio_ganadero",
            "scene": {"time": "06:00", "place": "Finca"},
        },
    )
    assert response.status_code == 404


def test_simulate_sin_persona_id(client: TestClient):
    """POST /v1/simulate sin persona_id retorna 422 (validacion Pydantic)."""
    response = client.post(
        "/v1/simulate",
        json={
            "city_id": "tello",
            "scene": {"time": "08:00", "place": "Plaza"},
        },
    )
    assert response.status_code == 422


def test_simulate_temperature_fuera_de_rango(client: TestClient):
    """POST /v1/simulate con temperature > 2.0 retorna 422."""
    response = client.post(
        "/v1/simulate",
        json={
            "city_id": "tello",
            "persona_id": "dona_rosa_tendera",
            "scene": {"time": "08:00", "place": "Tienda"},
            "temperature": 5.0,  # fuera de rango
        },
    )
    assert response.status_code == 422
