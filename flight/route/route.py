import os
import secrets
import flight.flights.index as search
from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint)




register = Blueprint('register', __name__)


@register.route('/', methods=['GET', 'POST'])
def index():
    
    return search['kiwi']()