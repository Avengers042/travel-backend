from typing import Any, Sequence
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session

from database.connection import get_session
from models.user import User
from repositories import user_repository
from schemas.user.user_schema import UserSchema


router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/",
    status_code=200,
    response_model=list[User],
    responses={500: {"description": "Problemas nos servidores"}},
)
def get_users(*, session: Session = Depends(get_session)) -> Sequence[User]:
    try:
        users = user_repository.get_all_users(session)
    except Exception:
        raise HTTPException(status_code=500, detail="Problemas no servidores")
    return users


@router.get(
    "/{id}",
    status_code=200,
    response_model=UserSchema,
    responses={
        404: {"description": "Usuário não encontrado"},
        500: {"description": "Problemas nos servidores"},
    },
)
def get_user_by_id(*, session: Session = Depends(get_session), id: int) -> Any:
    try:
        user = user_repository.get_user_by_id(session, id)
    except TypeError as e:
        return JSONResponse(status_code=404, content={"message": f"{e}"})
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "Problemas no servidores"}
        )
    return user


@router.post(
    "/",
    status_code=201,
    response_model=dict[str, str],
    responses={500: {"description": "Problemas nos servidores"}},
)
def create_user(*, session: Session = Depends(get_session), user: UserSchema) -> Any:
    try:
        user_model = User(name=user.name, email=user.email)
        user_repository.create_user(session, user_model)
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "Problemas no servidores"}
        )
    return JSONResponse(content={"message": "O usuário foi criado com sucesso"})


@router.put(
    "/{id}",
    status_code=200,
    responses={
        404: {"description": "Usuário não encontrado"},
        500: {"description": "Problemas nos servidores"},
    },
)
def update_user(*, session: Session = Depends(get_session), id: int, user: UserSchema):
    try:
        user_repository.update_user(session, id, user)
    except TypeError as e:
        return JSONResponse(status_code=404, content={"message": f"{e}"})
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "Problemas no servidores"}
        )
    return JSONResponse(content={"message": "Usuário atualizado com sucesso"})
