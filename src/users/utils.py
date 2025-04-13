import bcrypt


def get_hashed(plain: str) -> str:
    plain_bytes = plain.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=plain_bytes, salt=salt)
    return hashed_password.decode('utf-8')


def is_correct(plain: str, hashed: str) -> bool:
    plain_bytes = plain.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)
