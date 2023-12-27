from . import happymeet
from flask import render_template

@happymeet.route('/meet')
def meet():
    return render_template('meetinghome.html')