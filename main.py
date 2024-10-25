from fastapi import FastAPI
from src.controllers.home_controller import router as home_router
from src.controllers.viagem_controller import router as viagem_router
from src.controllers.passagem_controller import router as passagem_router

app = FastAPI()

app.include_router(home_router)
app.include_router(viagem_router)
app.include_router(passagem_router)


