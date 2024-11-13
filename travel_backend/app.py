from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import api

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:5000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
