from fastapi import APIRouter

from users.fastapi_users_instance import fastapi_users_instance, auth_backend
from users.schemas import UserRead, UserCreate, UserUpdate


router = APIRouter()

router.include_router(
    fastapi_users_instance.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users_instance.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users_instance.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users_instance.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users_instance.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)