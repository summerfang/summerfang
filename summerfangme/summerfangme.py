from flask import Blueprint, redirect, render_template, request
import os

import configcatclient
from articledb.article import answer_question
# import logging

from webex.webex import send_message2Summer
from articledb.article import answer_question

# from . import summerfang

# logging.basicConfig(level=logging.INFO)

CONFIGCAT_KEY = os.getenv("CONFIGCAT_KEY")

configcat_client = configcatclient.get(CONFIGCAT_KEY)

# isMyFirstFeatureEnabled = configcat_client.get_value('isMyFirstFeatureEnabled', False)
isTagsEnabled = configcat_client.get_value('isTagsEnabled', False)

# print('isMyFirstFeatureEnabled\'s value from ConfigCat: ' + str(isMyFirstFeatureEnabled))
print('isTagsEnabled\'s value from ConfigCat: ' + str(isTagsEnabled))
CONFIGCAT_KEY = os.getenv("CONFIGCAT_KEY")

configcat_client = configcatclient.get(CONFIGCAT_KEY)

# isMyFirstFeatureEnabled = configcat_client.get_value('isMyFirstFeatureEnabled', False)
isTagsEnabled = configcat_client.get_value('isTagsEnabled', False)

# print('isMyFirstFeatureEnabled\'s value from ConfigCat: ' + str(isMyFirstFeatureEnabled))
print('isTagsEnabled\'s value from ConfigCat: ' + str(isTagsEnabled))

summerfang = Blueprint('summerfang', __name__, template_folder='templates', static_folder='static')

@summerfang.route('/') 
@summerfang.route('/index')
@summerfang.route('/home')
def index():
    if request.host == 'happymeet.me':
        return redirect('/meet')
    return render_template('home.html', CONFIGCAT_KEY=CONFIGCAT_KEY)

@summerfang.route('/about')
def about():
    return render_template('about.html', title='About')

@summerfang.route('/architecture')
def architecture():
    return render_template('architecture.html')

@summerfang.route('/engineering')
def engineering():
    return render_template('engineering.html')

@summerfang.route('/askSummer', methods=['GET', 'POST'])
def askSummer():
    if request.method == 'POST':
        question = request.form['question']
        answer = answer_question(question=question)

        if answer == "I don't know.":
            return send_message2Summer(question)
    return answer
