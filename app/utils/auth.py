from jose import jwt
import time

SECRET = "SECRET_KEY"

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = time.time() + 3600
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token

def decode_token(token: str):
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        return data
    except:
        return None
