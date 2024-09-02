from sqlmodel import SQLModel
from travel_backend.database.connection import engine

SQLModel.metadata.create_all(engine)
