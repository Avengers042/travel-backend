from fastapi.middleware.cors import CORSMiddleware

from config.cors import ORIGINS_ALLOWED


class CORSSettings:
    middleware_class = CORSMiddleware
    origins = ORIGINS_ALLOWED
    allow_credentials = True
    allow_methods = ["*"]
    allow_headers = ["*"]
