import os

from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

from twilio.rest import Client

from summerfangme.summerfangme import summerfang
from happymeetme import happymeet

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    try:
        data = request.get_json()

        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Test from summerfang.me",
            from_="+18559563669",
            to="4088323545",
        )


        # Your Twilio logic here
        # ...
        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)
    
if __name__ == '__main__':
    app.run(debug=True)