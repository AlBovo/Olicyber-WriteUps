#!/usr/bin/env python3
import requests

# guardando nelle richieste delle api si nota che si possono vedere tutte le note di un utente
SITE = "http://naas.challs.olicyber.it/api/debug/notes/1" # note dell'admin

r = requests.get(SITE)
print(r.json()["Notes"][1]['idea_name'])