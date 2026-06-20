"""
POST /v1/simulate — genera dialogo LLM para una persona en una escena.

En S1: skeleton con validacion Pydantic y respuesta mock honesta.
En S2: integra motor_simulacion.prompt_builder + DeepSeek via OpenAI-compatible.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

router = APIRouter()


class Scene(BaseModel):
    time: str = Field(..., description="Hora del dia, formato HH:MM")
    place: str = Field(..., description="Lugar fisico de la escena")
    weather: str | None = Field(None, description="Clima opcional")


class SimulateRequest(BaseModel):
    city_id: str = Field(default="tello", description="ID de la ciudad")
    persona_id: str = Field(..., description="ID de la persona a simular")
    scene: Scene
    model: str = Field(default="deepseek-chat", description="Modelo LLM a usar")
    temperature: float = Field(default=1.3, ge=0.0, le=2.0)


class SimulateMetadata(BaseModel):
    cost_usd: float
    latency_ms: int
    tokens_in: int
    tokens_out: int
    model: str
    temperature: float
    best_of_n_score: float | None = None


class SimulateResponse(BaseModel):
    text: str
    metadata: SimulateMetadata


@router.post("/simulate", response_model=SimulateResponse)
def simulate(request: SimulateRequest):
    """Genera un dialogo LLM para la persona en la escena dada.

    S1: skeleton con respuesta placeholder honesta.
    S2: integracion real con motor_simulacion + DeepSeek.
    """
    # Validacion basica
    if request.city_id != "tello":
        raise HTTPException(status_code=404, detail=f"Ciudad '{request.city_id}' no encontrada")

    if not request.persona_id:
        raise HTTPException(status_code=400, detail="persona_id requerido")

    # S1: respuesta placeholder honesta (mismo patron que el protito)
    return SimulateResponse(
        text=(
            f"[Simulacion LLM no disponible en este momento. "
            f"El backend DeepSeek requiere deploy. "
            f"Persona: {request.persona_id}, "
            f"escena: {request.scene.time} en {request.scene.place}. "
            f"Los datos psicometricos y la red mostrados son datos validados.]"
        ),
        metadata=SimulateMetadata(
            cost_usd=0.0,
            latency_ms=0,
            tokens_in=0,
            tokens_out=0,
            model=request.model,
            temperature=request.temperature,
            best_of_n_score=None,
        ),
    )
