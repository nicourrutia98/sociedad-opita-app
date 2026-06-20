"""
GET /v1/cities — lista las ciudades disponibles
GET /v1/cities/{city_id}/personas — personas de una ciudad

En S1: retorna data estatica embebida (los 41 personas de Tello validadas).
En S2+: carga desde S3 o DynamoDB.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal

router = APIRouter()


# Pydantic models
class City(BaseModel):
    city_id: str
    display_name: str
    available_personas: int


class CityListResponse(BaseModel):
    cities: list[City]


class Persona(BaseModel):
    persona_id: str
    display_name: str
    role: str
    age: int
    gender: Literal["M", "F"]
    archetype: str
    muletillas: list[str] = []


class PersonaListResponse(BaseModel):
    personas: list[Persona]


# Data estatica v1 — 41 personas validadas de Tello, Huila
# En S2+, esto migra a S3/DynamoDB
TELLO_PERSONAS: list[dict] = [
    {"persona_id": "don_rosalio_ganadero", "display_name": "Don Rosalio", "role": "ganadero_propietario", "age": 62, "gender": "M", "archetype": "ganadero_tradicional", "muletillas": ["asina es la cosa", "le digo yo", "ni muerto"]},
    {"persona_id": "dona_rosa_tendera", "display_name": "Doña Rosa Elvira", "role": "tendera_fiadera", "age": 55, "gender": "F", "archetype": "tendero_pueblo", "muletillas": ["mira ve", "le cuento", "eso si es verriondo"]},
    {"persona_id": "padre_cecilio_sacerdote", "display_name": "Padre Cecilio", "role": "parroco", "age": 56, "gender": "M", "archetype": "sacerdote_rural", "muletillas": ["Dios es el que sabe", "mijo", "rezaremos por ello"]},
    {"persona_id": "dona_prudencia_viuda", "display_name": "Doña Prudencia", "role": "viuda_anfitriona", "age": 71, "gender": "F", "archetype": "viuda_anfitriona", "muletillas": ["Dios mediante", "Ave Maria Purisima", "pues si mijita"]},
    {"persona_id": "jhon_eliecer_jornalero", "display_name": "Jhon Eliécer", "role": "jornalero", "age": 48, "gender": "M", "archetype": "trabajador_rural", "muletillas": ["pues mira ve", "le cuento", "eso si es verriondo"]},
    {"persona_id": "don_octavio_medico", "display_name": "Don Octavio", "role": "medico_tradicional", "age": 78, "gender": "M", "archetype": "medico_tradicional", "muletillas": ["eso no es asi", "fijese pues", "le digo por su bien"]},
    {"persona_id": "don_emigdio_agricultor", "display_name": "Don Emigdio", "role": "agricultor_caficultor", "age": 64, "gender": "M", "archetype": "trabajador_rural", "muletillas": ["si Dios quiere", "pues si", "hay que trabajar"]},
    {"persona_id": "don_eliecer_patron", "display_name": "Don Eliécer", "role": "finquero_patron", "age": 58, "gender": "M", "archetype": "ganadero_tradicional", "muletillas": ["le digo yo", "eso no se hace", "hagale pues"]},
    {"persona_id": "jhon_jairo_sacristan", "display_name": "Jhon Jairo", "role": "sacristan_peregrino", "age": 52, "gender": "M", "archetype": "artesano_independiente", "muletillas": ["con Dios", "Ave Maria", "Dios mediante"]},
    {"persona_id": "jhon_fredy_joven", "display_name": "Jhon Fredy", "role": "joven_retornado", "age": 28, "gender": "M", "archetype": "joven_migrante", "muletillas": ["parce", "nojoda", "esa vaina"]},
    # 31 personas más (skeleton) — se completan en S2
]


@router.get("", response_model=CityListResponse)
def list_cities():
    """Lista las ciudades disponibles."""
    return CityListResponse(
        cities=[
            City(
                city_id="tello",
                display_name="Tello, Huila",
                available_personas=len(TELLO_PERSONAS),
            )
        ]
    )


@router.get("/{city_id}/personas", response_model=PersonaListResponse)
def list_personas(city_id: str):
    """Retorna las personas de una ciudad."""
    if city_id != "tello":
        raise HTTPException(status_code=404, detail=f"Ciudad '{city_id}' no encontrada")

    return PersonaListResponse(
        personas=[Persona(**p) for p in TELLO_PERSONAS]
    )
