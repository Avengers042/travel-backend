from sqlmodel import Field
from schemas.user.user_schema import UserSchema


class User(UserSchema, table=True):
    id: int | None = Field(default=None, primary_key=True)
