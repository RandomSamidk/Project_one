import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import dotenv
import jwt
from fastapi import HTTPException

dotenv.load_dotenv()

SECRET_KEY: str = os.getenv("secret", "")
ALGORITHM: str = os.getenv("algorithm", "")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate a signed JWT."""
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Return claims if token is valid; raise 401 otherwise."""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
