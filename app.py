from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
        question = request.get_json()
        print(question)

    result = [{'question': 'I asdf good'}, {'pro','dd'}]
    return jsonify(result)
