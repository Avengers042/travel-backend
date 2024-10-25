from fastapi import APIRouter

router = APIRouter()

@router.get("/viagem")
async def viagem():
    return "viagem content"

@router.post("/viagem/preferencias")
async def viagem_preferencias():
    return "preferencias"

@router.post("/viagem/recomendacoes")
async def viagem_recomendacoes():
    return "recomendacoes"
