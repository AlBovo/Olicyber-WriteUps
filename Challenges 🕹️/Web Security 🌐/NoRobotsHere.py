import requests
from bs4 import BeautifulSoup
site = "http://no-robots.challs.olicyber.it"
r = requests.get(f"{site}/robots.txt")
r1 = requests.get(f"{site}/I77p0mhKjr.html")
b = BeautifulSoup(r1.text, 'html.parser')
print(str(b.find_all("h2")[0]).replace("<h2>", "").replace("</h2>", ""), end="")