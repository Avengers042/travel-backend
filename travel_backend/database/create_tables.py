from sqlmodel import SQLModel
from travel_backend.database.connection import engine
from travel_backend.models import user

SQLModel.metadata.create_all(engine)
