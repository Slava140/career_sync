from datetime import datetime
from typing import Annotated

from sqlalchemy import String, DateTime, text
from sqlalchemy.orm import mapped_column


sql_utc_now = text("timezone('utc', now())")

str_255 = Annotated[str, 255]
str_255_unique = Annotated[str, mapped_column(String(255), unique=True)]

created_at = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=sql_utc_now)]
updated_at = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=sql_utc_now, onupdate=sql_utc_now)]
datetime_tz = Annotated[datetime, mapped_column(DateTime(timezone=True))]


pk_int = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

