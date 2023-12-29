from flask import Blueprint, render_template

happymeet = Blueprint('my_happymeet', __name__, template_folder='templates', static_folder='static')

from . import happymeetme