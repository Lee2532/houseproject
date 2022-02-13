from rest_framework.response import Response
from rest_framework.exceptions import APIException

import jwt
import os
import datetime

SECRET = os.environ.get("SECRET_KEY")


def get_token(data):
    exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    # exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
    payload = {
        "username" : data.get('username', None),
    }
    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    
    token = jwt.encode(payload, SECRET, algorithm = 'HS256')
    return token


def check_token(access_token):
    try:
        decoded = jwt.decode(access_token, SECRET, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        raise APIException("TOKEN_EXPIRED")
    return decoded