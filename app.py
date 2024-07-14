import os

from flask import Flask, redirect, request, jsonify
from flask_cors import CORS, cross_origin
# from flask_socketio import SocketIO, emit
from flask_socketio import SocketIO

# from twilio.rest import Client

# from summerfangme.summerfangme import summerfang
# from happymeetme import happymeet

# from trueup.receivesms import receive_recent_7days_messages_by

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://localhost:5000","https://www.gettrueup.com", "https://gettrueup.com"]}})

# app.register_blueprint(summerfang, url_prefix='/summerfang')
# app.register_blueprint(happymeet, url_prefix='/meet')

CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

# socketio = SocketIO(app, cors_allowed_origins="*")
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     if request.host == 'happymeet.me' or request.host == 'www.happymeet.me':
#         return redirect('/meet')
#     else:
#         return redirect('/summerfang')

# @app.route('/api/greeting/<string:name>', methods=['GET'])
# def greet(name):
#     return jsonify(greeting=f"Hello, {name}!")

# @app.route('/api/messages', methods=['POST'])
# def send_message():
#     if 'x-api-key' not in request.headers:
#         print("No x-api-key in headers")
#         return jsonify(success=False), 401
#     if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
#         print("x-api-key does not match")
#         print(request.headers['x-api-key'] + " != " + os.environ['REACT_APP_X_API_KEY'])
#         return jsonify(success=False), 401  
    
#     try:
#         data = request.get_json()
#         print("-")
#         print(data)
#         print("-")
#         account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#         auth_token = os.environ["TWILIO_AUTH_TOKEN"]
#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             body=data['body'],
#             from_=data['from'],
#             to=data['to'],
#         )

#         return jsonify(success=True)
#     except Exception as e:
#         print(e)
#         return jsonify(success=False)
    
# @app.route('/api/allmessages', methods=['POST'])
# def send_allmessages():
#     if 'x-api-key' not in request.headers:
#         print("No x-api-key in headers")
#         return jsonify(success=False), 401
#     if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
#         print("x-api-key does not match")
#         return jsonify(success=False), 401
    
#     try:
#         data = request.get_json()
#         account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#         auth_token = os.environ["TWILIO_AUTH_TOKEN"]
#         client = Client(account_sid, auth_token)

#         # print(data)

#         for message in data:
#             message = client.messages.create(
#                 body=message['body'],
#                 from_=message['from'],
#                 to=message['to'],
#             )


#         return jsonify(success=True)

#     except Exception as e:
#         print(e)
#         return jsonify(success=False)

@app.route('/sms', methods=['POST'])
# @cross_origin(origins="*")  # This will allow /sms to be accessed from any domain
def receive_message():
    print(request.form)
    socketio.emit('new message', request.form)
    return jsonify(success=True)

@app.route('/smserror', methods=['POST'])
# @cross_origin(origins="*")  # This will allow /sms to be accessed from any domain
def receive_error_message():
    print(request.form)
    return jsonify(success=True)

# @app.route('/api/viewallmessages', methods=['POST'])
# def get_all_messages():
#     if 'x-api-key' not in request.headers:
#         print("No x-api-key in headers")
#         return jsonify(success=False), 401
#     if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
#         print("x-api-key does not match")
#         return jsonify(success=False), 401
    
#     try:
#         # data = request.get_json()
#         # account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#         # auth_token = os.environ["TWILIO_AUTH_TOKEN"]
#         # client = Client(account_sid, auth_token)

#         # messages = client.messages.list(
#         #     date_sent_after=data['date'],
#         #     from_=data['from'],
#         #     to=data['to'],
#         # )

#         messages = receive_recent_7days_messages_by()
#         print("----")
#         print(messages)
#         return jsonify(success=True, messages=messages)

#     except Exception as e:
#         print(e)
#         return jsonify(success=False)
    
# @app.route('/api/receive_recent_messages_by', methods=['POST'])
# def receive_recent_messages():
#     if 'x-api-key' not in request.headers:
#         print("No x-api-key in headers")
#         return jsonify(success=False), 401
#     if request.headers['x-api-key'] != os.environ['REACT_APP_X_API_KEY']:
#         print("x-api-key does not match")
#         return jsonify(success=False), 401
    
#     try:
#         data = request.get_json()
#         account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#         auth_token = os.environ["TWILIO_AUTH_TOKEN"]
#         client = Client(account_sid, auth_token)

#         messages = client.messages.list(
#             date_sent_after=data['date'],
#             from_=data['from'],
#             to=data['to'],
#         )

#         msgs = [{
#                 'body': message.body,
#                 'date_sent': message.date_sent,
#                 'from': message.from_,
#                 'to': message.to,
#             } for message in messages]

#         return jsonify(success=True, messages=msgs)

#     except Exception as e:
#         print(e)
#         return jsonify(success=False)

if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, debug=True)