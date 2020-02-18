import os
import secrets
import flight.flights.index as search
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint)


flight = Blueprint('flight', __name__)


@flight.route('/flight', methods=['GET', 'POST'])
def index():
    a = 5
    print(a)
    return search['clairty']()