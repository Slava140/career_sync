from pydantic import BaseModel, EmailStr, ConfigDict

from apptypes.schemas import PasswordStr, NonEmptyStr255, DateTimeWithTimezone


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None

    model_config = ConfigDict(from_attributes=True)


class RegisterRequestBody(BaseModel):
    email: EmailStr
    password: PasswordStr
    first_name: NonEmptyStr255
    last_name: NonEmptyStr255
    patronymic: NonEmptyStr255 | None

    model_config = ConfigDict(from_attributes=True)


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