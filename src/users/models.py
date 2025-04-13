from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from apptypes.models import pk_int, str_255, str_255_unique, created_at, updated_at
from database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[pk_int]
    email: Mapped[str_255_unique]
    hashed_password: Mapped[str_255]
    first_name: Mapped[str_255]
    last_name: Mapped[str_255]
    patronymic: Mapped[str_255 | None]
    is_verified: Mapped[bool] = mapped_column(server_default=expression.false())
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
