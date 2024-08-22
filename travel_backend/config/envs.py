from functools import lru_cache
from dotenv import load_dotenv


@lru_cache
def load_envs():
    _ = load_dotenv()
