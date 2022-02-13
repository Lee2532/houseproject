from rest_framework.response import Response
from rest_framework.exceptions import APIException

import jwt
import os
import datetime
from user.models import User

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

class JWTLogin:
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        try:
            if token:
                token_payload = jwt.decode(token, SECRET, algorithms="HS256")
                username = User.objects.get(username=token_payload['username'])
                request.user = username
                return self.original_function(self, request, *args, **kwargs)
            # return APIException("INVALID_TOKEN", status=401)
            return Response({'messaege':'NEED_LOGIN'}, status=401)
        except jwt.ExpiredSignatureError:
            return Response({'messaege':'TOKEN_EXPIRED'}, status=401)
            # raise APIException("TOKEN_EXPIRED", status=401)
        except jwt.DecodeError:
            return Response({'messaege':'INVALID_TOKEN'}, status=401)
            # raise APIException({'message':'INVALID_TOKEN'}, status=401)
        except User.DoesNotExist:
            return Response({'messaege':'INVALID_USER'}, status=401)
            # raise APIException({'message':'INVALID_USER'}, status=401)    
        


def check_token(request):
    access_token = request.headers.get('Authorization', None)
    try:
        decoded = jwt.decode(access_token, SECRET, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        raise APIException("TOKEN_EXPIRED", status=401)
    except jwt.DecodeError:
        raise APIException({'message':'INVALID_USER'}, status=401)
    except User.DoesNotExist:
        raise APIException({'message':'INVALID_USER'}, status=401)
    return decoded

