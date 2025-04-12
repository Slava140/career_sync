from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session
from sqlalchemy.orm import DeclarativeBase, registry

from apptypes.models import str_255
from config import settings

engine = create_async_engine(settings.database_url_asyncpg)
session_maker = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str_255: String(255),
        }
    )
