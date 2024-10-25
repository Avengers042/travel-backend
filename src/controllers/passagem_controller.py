from fastapi import APIRouter

router = APIRouter()

@router.get("/passagem")
async def passagem():
    return "viagem content"

@router.post("/passagem/recomendar")
async def passagem_recomendar():
    return "preferencias"

