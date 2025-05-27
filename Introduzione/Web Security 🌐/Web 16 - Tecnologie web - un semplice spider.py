from bs4 import BeautifulSoup
import requests
l = {}
site = "http://web-16.challs.olicyber.it"
p = [""]
while True:
    for pos in p: 
        r = requests.get(site + pos)
        print(site+pos)
        zuppetta = BeautifulSoup(r.text, "html.parser")
        if "flag" in r.text:
            print(zuppetta.find('h1'))
            exit(0)
        print(zuppetta.find('h1'))
        for i in zuppetta.find_all("a", href=True):
            if i['href'] not in l:
                l[i['href']] = True
                p.append(i['href'])
                r.close()