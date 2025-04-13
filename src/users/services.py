from typing import TYPE_CHECKING

from fastapi import HTTPException

from users.schemas import RegisterRequestBody, NonExistentUser, ExistingUser

if TYPE_CHECKING:
    from users.dao import UserDAO


class UserService:
    def __init__(self, users_dao: "UserDAO"):
        self.dao = users_dao

    async def register(self, schema: NonExistentUser) -> ExistingUser:
        async with self.dao:
            user = await self.dao.get_by_email(str(schema.email))
            if user:
                raise HTTPException(409, 'Already exists')
            created_user = await self.dao.add(schema)


        return created_user


