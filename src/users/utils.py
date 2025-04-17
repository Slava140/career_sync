from datetime import datetime, timezone

import bcrypt
import jwt

from config.jwt import jwt_settings


def get_hashed(plain: str) -> str:
    plain_bytes = plain.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=plain_bytes, salt=salt)
    return hashed_password.decode('utf-8')


def is_correct(plain: str, hashed: str) -> bool:
    plain_bytes = plain.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)


def create_access_token(user_id: int):
    now = datetime.now(timezone.utc)
    return jwt.encode(
        dict(sub=user_id, iat=now, exp=now + jwt_settings.access_token_lifetime_timedelta),
        jwt_settings.SECRET
    )
