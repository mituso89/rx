from flight.config import Config
import os
import secrets

import flight.controllers.flightctl as search
import jwt
import datetime
from flight.config import Config
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint, request, jsonify)


flight = Blueprint('flight', __name__)


@flight.route('/get/flights', methods=['GET', 'POST'])
def index():

    return search.flightctl(request.get_json())


@flight.route('/login', methods=['POST'])
def login():
    token = jwt.encode({
        'email': request.get_json()['email'],
        'password': request.get_json()['password'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    }, Config.SECRET_TOKEN)

    return jsonify({'token': token.decode('utf-8')})
