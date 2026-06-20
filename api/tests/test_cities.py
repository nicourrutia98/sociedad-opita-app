"""
Smoke tests para /v1/cities y /v1/cities/:id/personas.

Estos tests verifican el contrato del API end-to-end sin tocar LLM ni DynamoDB.
"""

from fastapi.testclient import TestClient


def test_health(client: TestClient):
    """GET /health retorna status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "sociedad-opita-api"


def test_list_cities(client: TestClient):
    """GET /v1/cities retorna al menos Tello."""
    response = client.get("/v1/cities")
    assert response.status_code == 200
    cities = response.json()["cities"]
    assert len(cities) >= 1

    tello = next((c for c in cities if c["city_id"] == "tello"), None)
    assert tello is not None
    assert tello["display_name"] == "Tello, Huila"
    assert tello["available_personas"] >= 1


def test_list_personas_tello(client: TestClient):
    """GET /v1/cities/tello/personas retorna personas con shape valido."""
    response = client.get("/v1/cities/tello/personas")
    assert response.status_code == 200
    personas = response.json()["personas"]
    assert len(personas) >= 1

    # Verificar shape del primer persona
    p = personas[0]
    required_fields = ["persona_id", "display_name", "role", "age", "gender", "archetype"]
    for field in required_fields:
        assert field in p, f"Falta campo {field} en persona {p.get('persona_id')}"

    # Verificar que Dona Rosa esta (personaje iconic, super-spreader #1)
    rosa = next((p for p in personas if p["persona_id"] == "dona_rosa_tendera"), None)
    assert rosa is not None, "Dona Rosa (super-spreader) debe estar en la lista"
    assert rosa["archetype"] == "tendero_pueblo"
    assert len(rosa["muletillas"]) >= 1, "Dona Rosa debe tener muletillas"


def test_list_personas_ciudad_inexistente(client: TestClient):
    """GET /v1/cities/inexistente/personas retorna 404."""
    response = client.get("/v1/cities/garzon_inexistente/personas")
    assert response.status_code == 404
    assert "no encontrada" in response.json()["detail"].lower()
