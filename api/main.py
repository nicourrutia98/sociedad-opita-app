"""
Sociedad Opita API — FastAPI + Mangum handler para AWS Lambda.

Stack:
- FastAPI: framework HTTP async
- Mangum: adapter ASGI -> AWS Lambda + API Gateway
- AWS Lambda Powertools: logging, tracing, metrics
- Motor de simulacion: import desde api/motor/ (copia local)

Endpoints (v1):
- GET  /v1/cities                  -> lista de ciudades disponibles
- GET  /v1/cities/{id}/personas    -> personas de una ciudad
- POST /v1/simulate                -> genera dialogo LLM para una persona
- GET  /v1/stream                  -> SSE stream del pueblo (S2)
- WS   /v1/chat                    -> WebSocket chat con personajes (S2)

Deploy: ver infra/aws/template.yaml
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from aws_lambda_powertools import Logger

from api.routes import cities, simulate

logger = Logger(service="sociedad-opita-api")

app = FastAPI(
    title="Sociedad Opita API",
    description="Backend del monumento cultural vivo — simulación social de Tello, Huila",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
)

# CORS — el frontend en sociedad.opitacode.com (Cloudflare Pages) llama a este API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sociedad.opitacode.com",
        "https://www.sociedad.opitacode.com",
        "http://localhost:4321",  # dev local
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health")
def health():
    return {"status": "ok", "service": "sociedad-opita-api"}


# Routes
app.include_router(cities.router, prefix="/v1/cities", tags=["cities"])
app.include_router(simulate.router, prefix="/v1", tags=["simulate"])


# Mangum handler — punto de entrada para AWS Lambda
# API Gateway manda el evento en formato AWS_PROXY, Mangum lo convierte a ASGI
handler = Mangum(app, lifespan="off")
