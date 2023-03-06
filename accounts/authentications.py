import jwt
import datetime
from datetime import timezone


def encode_token(id):
    en_token = jwt.encode({"user": id, "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=24)}, "secret", algorithm="HS256")
    return en_token


def decode_token(token):
    de_token = jwt.decode(token, "secret", algorithms=["HS256"])
    return de_token
