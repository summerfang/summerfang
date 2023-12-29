from . import happymeet
from flask import render_template

@happymeet.route('/')
def meet():
    return render_template('meetinghome.html')