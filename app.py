from flask import Flask

from summerfangme.summerfangme import summerfang
from happymeetme import happymeet

app = Flask(__name__)
app.register_blueprint(summerfang)
app.register_blueprint(happymeet)


if __name__ == '__main__':
    app.run(debug=True)