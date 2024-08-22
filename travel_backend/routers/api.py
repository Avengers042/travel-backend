from fastapi import APIRouter

router = APIRouter(
    prefix="/api", tags=["api"], responses={404: {"description": "URL not found"}}
)


@router.get("/")
def get():
    return {"teste": "Ola"}
