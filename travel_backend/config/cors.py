from os import getenv
from travel_backend.config.envs import load_envs

load_envs()

ORIGINS_ALLOWED = getenv("DOMAIN_URL", "localhost:4200")