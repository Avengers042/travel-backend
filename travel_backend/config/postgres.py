from os import getenv
from pydantic_core import MultiHostUrl

from travel_backend.config.envs import load_envs

load_envs()

POSTGRES_HOST = getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(getenv("POSTGRES_PORT", "5432"))
POSTGRES_USER = getenv("POSTGRES_HOST", "postgres")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "123123")
POSTGRES_DB = getenv("POSTGRES_DB", "default")
SQLALCHEMY_DATABASE_URI = MultiHostUrl.build(
    scheme="postgresql+psycopg",
    username=POSTGRES_HOST,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    path=POSTGRES_DB,
)
