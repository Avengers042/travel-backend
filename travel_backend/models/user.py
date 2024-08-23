from sqlmodel import Field
from travel_backend.schemas.user.user_schema import UserSchema


class User(UserSchema, table=True):
    id: int | None = Field(default=None, primary_key=True)
