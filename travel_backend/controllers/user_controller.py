from typing import Any, Sequence
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session

from database.connection import get_session
from models.preferences import Preferences
from repositories import user_repository
from schemas.user.user_schema import UserSchema


router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/preferences",
    status_code=200,
    responses={200: {"description": "Problemas nos servidores"}},
)
def user_preferences(preferences: Preferences):
    return preferences

@router.get(
    "/preferences/recommendation",
    status_code=200,
    responses={200: {"description": "Problemas nos servidores"}},
)
def user_preferences_recommendation():
    example = {
            "place":"Rio de Janeiro",
            "description":"city",
            "accommodation":"Hotel fasano",
            "place_to_buy":"decolar"
            }
    data = jsonable_encoder(example)
    return JSONResponse(content=data)

