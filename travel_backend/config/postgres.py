from os import getenv
from pydantic_core import MultiHostUrl

from travel_backend.config.envs import load_envs

load_envs()

POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "123123")
POSTGRES_DB = getenv("POSTGRES_DB", "default")

SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
