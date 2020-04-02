from flight.config import Config
import os
import secrets

import flight.controllers.flightctl as search
import jwt
import datetime
import flight.common.common as cm
from flight.config import Config
import time
import flight.middleware.auth as authen
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint, request, jsonify, request)


flight = Blueprint('flight', __name__)


@flight.route('/get/flights', methods=['GET', 'POST'])
def index():
    # return 'tuan'
    return search.flightctl(request.get_json())


@flight.route('/login', methods=['POST'])
def login():
    if 'email' in request.get_json() and 'password' in request.get_json():
        token = jwt.encode({
            'email': request.get_json()['email'],
            'password': request.get_json()['password'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }, Config.SECRET_TOKEN)
    else:
        return jsonify({'message': 'Missing Token'}), 403

    result = {
        "success": True,
        "data": {
            "auth_token": token.decode('utf-8')
        }
    }
    return jsonify(result)


@flight.before_request
def genericSecure():
    if request.path in ('/login', '/token'):
        return
    print(request)
    if(request.headers.get('x-access-token') == None or request.headers.get('x-key') == None):
        return jsonify({'message': 'Missing Token'}), 403

    token = request.headers.get('x-access-token')
    payload = jwt.decode(token, Config.SECRET_TOKEN)
    timestamp = int(time.mktime(datetime.datetime.utcnow().timetuple()))
    if (timestamp> payload['exp']):
        return jsonify({'message': 'token expired'}), 403
    User = cm.FetchAccount(request.headers.get('x-key'))
    if User == None:
        return jsonify({'message': 'User not found'}), 403
    request.get_json()['User'] = User
    
    
