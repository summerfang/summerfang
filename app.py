import os

from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

from twilio.rest import Client

from summerfangme.summerfangme import summerfang
from happymeetme import happymeet

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://www.gettureup.com"]}})

app.register_blueprint(summerfang, url_prefix='/summerfang')
app.register_blueprint(happymeet, url_prefix='/meet')

@app.route('/')

def index():
    if request.host == 'happymeet.me' or request.host == 'www.happymeet.me':
        return redirect('/meet')
    else:
        return redirect('/summerfang')

@app.route('/api/greeting/<string:name>', methods=['GET'])
def greet(name):
    return jsonify(greeting=f"Hello, {name}!")

@app.route('/api/messages', methods=['POST'])
def send_message():
    if 'REACT_APP_X_API_KEY' not in request.headers:
        return jsonify(success=False), 401
    if request.headers['REACT_APP_X_API_KEY'] != os.environ['REACT_APP_X_API_KEY']:   
        return jsonify(success=False), 401  
    
    try:
        data = request.get_json()
        print("-")
        print(data)
        print("-")
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=data['body'],
            from_=data['from'],
            to=data['to'],
        )


        # Your Twilio logic here
        # ...
        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)

@app.route('/api/allmessages', methods=['POST'])
def send_allmessages():
    # Add logic if REACT_APP_X_API_KEY is not in the request headers, return 401
    # Add logic if REACT_APP_X_API_KEY is not equal to the value of X_API_KEY, return 401   
    if 'REACT_APP_X_API_KEY' not in request.headers:
        return jsonify(success=False), 401
    if request.headers['REACT_APP_X_API_KEY'] != os.environ['REACT_APP_X_API_KEY']:   
        return jsonify(success=False), 401  
    
    # Add logic to handle the body of the request, The body of the request is a JSON object which contains an array of objects. Each object contains the following keys:body, from, to
    # Add logic to send a message to each object in the array
    try:
        data = request.get_json()
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        for message in data:
            message = client.messages.create(
                body=message['body'],
                from_=message['from'],
                to=message['to'],
            )

        return jsonify(success=True)

    except Exception as e:
        print(e)
        return jsonify(success=False)
    
if __name__ == '__main__':
    app.run(debug=True)