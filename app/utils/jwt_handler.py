
import jwt
import dotenv 
import os
from fastapi import HTTPException
from datetime import datetime, timedelta , timezone

dotenv.load_dotenv()

SECRET_KEY = os.getenv('secret')
ALGORITHM = os.getenv('algorithm')

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    payload.update({"exp": expire})
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")