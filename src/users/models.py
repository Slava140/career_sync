from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

from apptypes.models import pk_int
from database import Base
from dependecies import get_async_db_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[pk_int]


async def get_user_db(db_session: AsyncSession = Depends(get_async_db_session)):
    yield SQLAlchemyUserDatabase(db_session, User)
