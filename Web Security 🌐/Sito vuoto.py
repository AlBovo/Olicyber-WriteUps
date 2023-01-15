import requests

site = "http://vuoto.challs.olicyber.it/"
html = requests.get(site)
for i in html.text.split("\n"):
    if "flag" in i:
        print(i)
        break
css = requests.get(f"{site}/css/style.css")
for i in css.text.split("\n"):
    if "flag" in i:
        print(i)
        break
js = requests.get(f"{site}/js/script.js")
for i in js.text.split("\n"):
    if "flag" in i:
        print(i)
        break