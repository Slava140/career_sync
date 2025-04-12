import re
from typing import Annotated

from annotated_types import MaxLen
from pydantic import AfterValidator, StringConstraints, Secret


def password_validator(value: str) -> str:
    if len(value) < 8:
        raise ValueError('Password length must be greater or equal than 8')

    if len(value) > 20:
        raise ValueError('Password length must be less or equal than 20')

    if not re.search(r'\d', value):
        raise ValueError('Password must contain at least one digit')

    if not re.search(r'[A-Z]', value):
        raise ValueError('Password must contain at least one uppercase letter')

    if not re.search(r'[a-z]', value):
        raise ValueError('Password must contain at least one lowercase letter')

    return value


NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Str255 = Annotated[NonEmptyStr, MaxLen(255)]
Str500 = Annotated[NonEmptyStr, MaxLen(500)]

RawPassword = Secret[Annotated[str, AfterValidator(password_validator)]]
HashedPassword = str
