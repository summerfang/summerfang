from flask import Flask, redirect, request

from summerfangme.summerfangme import summerfang
from happymeetme import happymeet

app = Flask(__name__)
app.register_blueprint(summerfang, url_prefix='/summerfang')
app.register_blueprint(happymeet, url_prefix='/meet')

@app.route('/')
def index():
    if request.host == 'happymeet.me' or request.host == 'www.happymeet.me':
        return redirect('/meet')
    else:
        return redirect('/summerfang')

if __name__ == '__main__':
    app.run(debug=True)