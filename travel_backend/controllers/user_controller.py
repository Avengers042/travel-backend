from typing import Any, Sequence
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session

from database.connection import get_session
from models.preferences import Preferences
from repositories import user_repository
from schemas.user.user_schema import UserSchema
from handlers.clips_handler import recommend_data


router = APIRouter(prefix="/preferences", tags=["preferences"])


@router.post(
    "/",
    status_code=200,
    responses={200: {"description": "Problemas nos servidores"}},
)
def user_preferences(preferences: Preferences):
    return preferences

@router.post(
    "/recommendation",
    status_code=200,
    responses={200: {"description": "Problemas nos servidores"}},
)
def user_preferences_recommendation(body: Any):
    print ('testeeeeeee')
    codeAsProperties = ['natureza', 'cultura', 'aventura', 'vidanoturna', 'hotel', 'airbnb', 'hostel', 'acampamento', 'equatorial', 'tropical', 'subtropical', 'massa', 'hamburger', 'sushi', 'churrasco', 'sobremesas']

    recomendantion = recommend_data(codeAsProperties[body['pontoTuristico']['codigo'] - 1], codeAsProperties[body['hospedagem']['codigo'] - 1], codeAsProperties[body['clima']['codigo'] - 1], codeAsProperties[body['alimentacao']['codigo'] - 1])

    print(recomendantion)

    example = {
            "cidade": recommend_data['cidade'],
            "ponto": recommend_data['categoria'],
            "descricao_ponto": recommend_data['descricao_ponto'],
            "descricao_alimentacao": recommend_data['descricao_alimentacao'],
            "descricao_hospedagem": recommend_data['descricao_hospedagem'],
            }
    print(example)
    data = jsonable_encoder(example)
    return JSONResponse(content=data)

