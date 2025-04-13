from typing import Annotated

from fastapi import Depends

from dependecies import DBSessionDep
from users.dao import UserDAO
from users.services import UserService


async def get_user_dao(db_session: DBSessionDep):
    return UserDAO(db_session)


UserDAODep = Annotated[UserDAO, Depends(get_user_dao)]


async def get_user_service(user_dao: UserDAODep):
    return UserService(user_dao)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
