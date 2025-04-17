from pydantic import BaseModel, EmailStr, ConfigDict, SecretStr

from apptypes.schemas import PasswordStr, NonEmptyStr255, DateTimeWithTimezone, NonEmptyStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None

    model_config = ConfigDict(from_attributes=True)


class JWTWithUserResponse(BaseModel):
    access_token: NonEmptyStr
    token_type: NonEmptyStr = 'bearer'
    user: UserResponse


class RegisterRequestBody(BaseModel):
    email: EmailStr
    password: PasswordStr
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None

    model_config = ConfigDict(from_attributes=True)


class LoginRequestBody(BaseModel):
    email: EmailStr
    password: SecretStr  # Не использую PasswordStr чтобы НЕ сообщать дополнительную информацию о пароле


class ExistingUser(BaseModel):
    """ используется для передачи данных между слоями """
    id: int
    email: EmailStr
    hashed_password: NonEmptyStr255
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None
    is_verified: bool
    created_at: DateTimeWithTimezone
    updated_at: DateTimeWithTimezone

    model_config = ConfigDict(from_attributes=True)


class NonExistentUser(BaseModel):
    email: EmailStr
    password: PasswordStr
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None
    is_verified: bool | None = None

    model_config = ConfigDict(from_attributes=True)