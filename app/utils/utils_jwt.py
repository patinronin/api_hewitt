from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse


def expire_date(days: int):
    date = datetime.now()
    expiration_date = date + timedelta(days)
    return expiration_date


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("API_KEY"),  algorithm="HS256")
    return token


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("API_KEY"), algorithms=["HS256"])
        decode(token, key=getenv("API_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
