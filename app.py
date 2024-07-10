import os

from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

from twilio.rest import Client

from summerfangme.summerfangme import summerfang
from happymeetme import happymeet

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://www.gettrueup.com", "https://gettrueup.com"]}})

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
    if 'x-api-key' not in request.headers:
        print("No x-api-key in headers")
        return jsonify(success=False), 401
    if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
        print("x-api-key does not match")
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

        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)

@app.route('/api/allmessages', methods=['POST'])
def send_allmessages():
    if 'x-api-key' not in request.headers:
        print("No x-api-key in headers")
        return jsonify(success=False), 401
    if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
        print("x-api-key does not match")
        return jsonify(success=False), 401
    
    try:
        data = request.get_json()
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        # print(data)

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