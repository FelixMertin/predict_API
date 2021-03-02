from functools import wraps
from flask import request
from flask_restplus import abort
from ..config import Config

def require_auth(func):
    """ Secure Method Decorator
    Compares the API Key in the request with the server-side stored API Key"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers.get('api-key'):
            api_key = request.headers.get('api-key')
        else:
            return abort(401)

        if api_key == Config.API_KEY:
            return func(*args, **kwargs)
        else:
            return abort(401)

    return wrapper