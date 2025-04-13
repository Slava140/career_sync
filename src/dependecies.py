from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import session_maker


async def get_async_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session


DBSessionDep = Annotated[AsyncSession, Depends(get_async_db_session)]