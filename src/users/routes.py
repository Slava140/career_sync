from fastapi import APIRouter

from users.schemas import RegisterRequestBody, NonExistentUser, LoginRequestBody, JWTWithUserResponse
from users.dependecies import UserServiceDep

router = APIRouter(prefix='/auth')


@router.post('/register')
async def register(body: RegisterRequestBody, user_service: UserServiceDep) -> JWTWithUserResponse:
    non_existing_user_schema = NonExistentUser.model_validate(body)
    existing_user_schema, access_token = await user_service.register(non_existing_user_schema)
    return JWTWithUserResponse(access_token=access_token, user=existing_user_schema)


@router.post('/login')
async def login(body: LoginRequestBody, user_service: UserServiceDep) -> JWTWithUserResponse:
    email, plain_password = body.email, body.password.get_secret_value()
    existing_user_schema, access_token = await user_service.login(email, plain_password)
    return JWTWithUserResponse(access_token=access_token, user=existing_user_schema)
