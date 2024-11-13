from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from handlers.clips_handler import recommend_data
from schemas.user.user_schema import Preferences


router = APIRouter(prefix="/preferences", tags=["preferences"])


@router.post(
    "/recommendation",
    status_code=200,
    responses={400: {"description": "Problemas nos servidores"}},
)
def user_preferences_recommendation(preferences: Preferences):
    codeAsProperties = [
        "natureza",
        "cultura",
        "aventura",
        "vidanoturna",
        "hotel",
        "airbnb",
        "hostel",
        "acampamento",
        "equatorial",
        "tropical",
        "subtropical",
        "massa",
        "hamburger",
        "sushi",
        "churrasco",
        "sobremesas",
    ]

    recomendantion = recommend_data(
        codeAsProperties[preferences.pontoTuristico - 1],
        codeAsProperties[preferences.hospedagem - 1],
        codeAsProperties[preferences.clima - 1],
        codeAsProperties[preferences.alimentacao - 1],
    )

    if not recomendantion:
        response = {
            "cidade": "Nenhuma cidade selecionada",
            "ponto": "Nenhuma categoria selecionada",
            "descricao_ponto": "Nenhuma descrição de categoria selecionada",
            "descricao_alimentacao": "Nenhum local de alimentação definido",
            "descricao_hospedagem": "Nenhum local de hospedagem definido",
        }
    else:
        response = {
            "cidade": recomendantion["cidade"],
            "ponto": recomendantion["ponto"],
            "descricao_ponto": recomendantion["descricao_ponto"],
            "descricao_alimentacao": recomendantion["descricao_alimentacao"],
            "descricao_hospedagem": recomendantion["descricao_hospedagem"],
        }

    data = jsonable_encoder(response)
    return JSONResponse(content=data)
