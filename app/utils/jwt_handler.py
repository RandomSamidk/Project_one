
import jwt
import dotenv 
import os
from datetime import datetime, timedelta

dotenv.load_dotenv()

SECRET_KEY = os.getenv('secret')
ALGORITHM = os.getenv('algorithm')

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    payload = data
    expire = datetime.now() + (expires_delta or timedelta(minutes=15))
    payload.update({"exp": expire})
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token