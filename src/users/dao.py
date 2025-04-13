from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User
from users.schemas import NonExistentUser, ExistingUser
from users.utils import get_hashed


class UserDAO:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def add(self, schema: NonExistentUser) -> ExistingUser:
        stmt = insert(
            User
        ).values(
            email=schema.email,
            hashed_password=get_hashed(schema.password.get_secret_value()),
            first_name=schema.first_name,
            last_name=schema.last_name,
            patronymic=schema.patronymic,
        ).returning('*')

        result = await self.db_session.execute(stmt)
        result_dict = result.mappings().one()

        return ExistingUser.model_validate(result_dict)

    async def get_by_email(self, email: str) -> ExistingUser | None:
        query = select(User).where(User.email == email)

        result = await self.db_session.execute(query)

        if user_model := result.scalar_one_or_none():
            return ExistingUser.model_validate(user_model)

    async def __aenter__(self):
        await self.db_session.begin()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            await self.db_session.commit()
        else:
            await self.db_session.rollback()
            raise
