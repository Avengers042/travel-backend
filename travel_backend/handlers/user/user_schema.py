from sqlmodel import SQLModel


class UserSchema(SQLModel):
    name: str
    email: str
