import os
import secrets
import flight.controllers.flightctl as search
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint, request, jsonify)


flight = Blueprint('flight', __name__)


@flight.route('/get/flights', methods=['GET', 'POST'])
def index():
    
    return search.flightctl(request.get_json())