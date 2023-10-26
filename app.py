from flask import Flask, render_template, request, jsonify
# from flask_talisman import Talisman

from webex.webex import send_message2Summer
from articledb.article import answer_question

app = Flask(__name__)
# Talisman(app)

@app.route('/') 
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/askSummer', methods=['GET', 'POST'])
def askSummer():
    if request.method == 'POST':
        question = request.form['question']
        answer = answer_question(question=question)

        if answer == "I don't know.":
            return send_message2Summer(question)
    return answer
