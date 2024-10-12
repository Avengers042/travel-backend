from sqlmodel import Session, create_engine
from config.postgres import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
