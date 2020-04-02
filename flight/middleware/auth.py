import jwt
import flight.common.common as cm
from flask import request, abort


def genericSecure(param):
    headers = param.headers
    if ['x-access-token'] in headers and 'x-key' in  headers:
        return cm({'message': 'x-access-token or x-key'}), 403

