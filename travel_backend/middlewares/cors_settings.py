from fastapi.middleware.cors import CORSMiddleware

from travel_backend.config.cors import ORIGINS_ALLOWED


class CORSSettings:
    middleware = CORSMiddleware
    origins = ORIGINS_ALLOWED
    allow_credentials = True
    allow_methods = ["*"]
    allow_headers = ["*"]
