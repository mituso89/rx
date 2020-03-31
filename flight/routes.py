import os
import secrets
import flight.controllers.flightctl as search
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint)


flight = Blueprint('flight', __name__)


@flight.route('/flight', methods=['GET', 'POST'])
def index():
    return search.flightctl('clairty')