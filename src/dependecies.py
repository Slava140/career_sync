from database import session_maker


async def get_async_db_session():
    async with session_maker() as session:
        yield session