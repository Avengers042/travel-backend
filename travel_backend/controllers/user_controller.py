from typing import Any
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from handlers.clips_handler import recommend_data


router = APIRouter(prefix="/preferences", tags=["preferences"])

@router.post(
    "/recommendation",
    status_code=200,
    responses={400: {"description": "Problemas nos servidores"}},
)
def user_preferences_recommendation(pontoTuristico: dict[str, Any], hospedagem: dict[str, Any], clima: dict[str, Any], alimentacao: dict[str, Any] = Body()):
    codeAsProperties = ['natureza', 'cultura', 'aventura', 'vidanoturna', 'hotel', 'airbnb', 'hostel', 'acampamento', 'equatorial', 'tropical', 'subtropical', 'massa', 'hamburger', 'sushi', 'churrasco', 'sobremesas']
    recomendantion = recommend_data(codeAsProperties[pontoTuristico.get("codigo") - 1], codeAsProperties[hospedagem.get("codigo") - 1], codeAsProperties[clima.get("codigo") - 1], codeAsProperties[alimentacao.get("codigo") - 1])

    example = {
            "cidade": recomendantion['cidade'],
            "ponto": recomendantion['ponto'],
            "descricao_ponto": recomendantion['descricao_ponto'],
            "descricao_alimentacao": recomendantion['descricao_alimentacao'],
            "descricao_hospedagem": recomendantion['descricao_hospedagem'],
    }

    data = jsonable_encoder(example)
    return JSONResponse(content=data)
