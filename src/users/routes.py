from fastapi import APIRouter

from users.schemas import UserResponse, RegisterRequestBody, NonExistentUser
from users.dependecies import UserServiceDep

router = APIRouter(prefix='/auth')


@router.post('/register')
async def register(body: RegisterRequestBody, user_service: UserServiceDep) -> UserResponse:
    non_existing_user_schema = NonExistentUser.model_validate(body)
    existing_user_schema = await user_service.register(non_existing_user_schema)

    return UserResponse.model_validate(existing_user_schema)
