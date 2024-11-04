from os import getenv
from config.envs import load_envs

load_envs()

ORIGINS_ALLOWED = [getenv("DOMAIN_URL", "localhost:4200")]
