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
    codeAsProperties = ['natureza', 'cultura', 'cultura e historia', 'aventura', 'vida noturna', 'hotel', 'airbnb', 'hostel', 'acampamento', 'equatorial', 'tropical', 'subtropical', 'massa', 'hamburger', 'sushi', 'churrasco', 'sobremesas']

    recomendantion = recommend_data(codeAsProperties[body['pontoTuristico']['codigo'] - 1], codeAsProperties[body['hospedagem']['codigo'] - 1], codeAsProperties[body['clima']['codigo'] - 1], codeAsProperties[body['alimentacao']['codigo'] - 1])

    print(recomendantion)

    example = {
            "place":"Rio de Janeiro",
            "description":"city",
            "accommodation":"Hotel fasano",
            "place_to_buy":"decolar"
            }
    data = jsonable_encoder(example)
    return JSONResponse(content=data)

