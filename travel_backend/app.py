from fastapi import FastAPI

from middlewares.cors_settings import CORSSettings

from routers import api

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:5000",
]

app = FastAPI()

app.add_middleware(
    middleware_class=CORSSettings.middleware_class,
    allow_origins=CORSSettings.origins,
    allow_credentials=CORSSettings.allow_credentials,
    allow_methods=CORSSettings.allow_methods,
    allow_headers=CORSSettings.allow_headers,
)

app.include_router(api.router)
