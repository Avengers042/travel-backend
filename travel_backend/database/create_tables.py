from sqlmodel import SQLModel
from database.connection import engine
from models import user

SQLModel.metadata.create_all(engine)
