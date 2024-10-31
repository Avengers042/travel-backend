from sqlmodel import Field
from fastapi import FastAPI
from pydantic import BaseModel
#from schemas.user.user_schema import UserSchema


class Preferences(BaseModel):
    tipo: str
    hospedagem: str
    clima: str
    alimento: str
