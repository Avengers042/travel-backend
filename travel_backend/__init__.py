from fastapi import FastAPI

from travel_backend.middlewares.cors_settings import CORSSettings
from travel_backend.routers import api


app = FastAPI()
cors = CORSSettings()

app.add_middleware(
    cors.middleware,
    cors.origins,
    allow_credentials=cors.allow_credentials,
    allow_methods=cors.allow_methods,
    allow_headers=cors.allow_headers,
)

app.include_router(api.router)
