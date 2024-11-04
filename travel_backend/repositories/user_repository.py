from typing import Sequence
from sqlmodel import Session, select

from models.user import User
from schemas.user.user_schema import UserSchema


def get_all_users(session: Session) -> Sequence[User]:
    statement = select(User)
    results = session.exec(statement).all()
    return results

def get_user_by_id(session: Session, id: int) -> User:
    user = session.get(User, id)
    if not user:
        raise TypeError("Usuário não encontrado")
    return user
    

def create_user(session: Session, user: User) -> None:
    session.add(user)
    session.commit()

def update_user(session: Session, id: int, to_be_user: UserSchema) -> None:
    user = session.get(User, id)

    if not user:
        raise TypeError("Usuário não encontrado")

    formated_user = to_be_user.model_dump(exclude_unset=True)
    user.sqlmodel_update(formated_user)
    session.add(user)
    session.commit()

