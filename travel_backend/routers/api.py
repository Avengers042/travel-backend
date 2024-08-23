from fastapi import APIRouter
from travel_backend.controllers import user_controller
from travel_backend.controllers import UserController

router = APIRouter(
    prefix="/api"
)

router.include_router(UserController)
