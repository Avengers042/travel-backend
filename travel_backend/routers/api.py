from fastapi import APIRouter
from controllers import UserController

router = APIRouter(prefix="/api")

router.include_router(UserController)
