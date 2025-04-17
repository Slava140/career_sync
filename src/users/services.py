from typing import TYPE_CHECKING

from fastapi import HTTPException

from users.schemas import NonExistentUser, ExistingUser
from users.utils import is_correct, create_access_token

if TYPE_CHECKING:
    from users.dao import UserDAO


class UserService:
    def __init__(self, users_dao: "UserDAO"):
        self.dao = users_dao

    async def register(self, schema: NonExistentUser) -> tuple[ExistingUser, str]:
        async with self.dao:
            user = await self.dao.get_by_email(str(schema.email))
            if user:
                raise HTTPException(409, 'Already exists')
            created_user = await self.dao.add(schema)
        access_token = create_access_token(created_user.id)
        return created_user, access_token

    async def login(self, email: str, password: str) -> tuple[ExistingUser, str]:
        user_with_email = await self.dao.get_by_email(email)
        if user_with_email and is_correct(password, user_with_email.hashed_password):
            access_token = create_access_token(user_with_email.id)
            return user_with_email, access_token
        else:
            raise HTTPException(401, 'Invalid email or password.')

