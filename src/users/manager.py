from fastapi import Depends
from fastapi_users import IntegerIDMixin, BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from config import settings
from users.models import User, get_user_db


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    verification_token_secret = settings.JWT_SECRET
    ...


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
