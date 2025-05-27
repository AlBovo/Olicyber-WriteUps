#!/usr/bin/env python3
import pyshark, re

REGEX = r'\.(.*?)\.'
cap = pyshark.FileCapture('capture.pcapng', display_filter='dns && ip.src == 10.0.1.1')

data = b''

for pkt in cap:
    dns = str(pkt.dns.qry_name)
    
    if 'attacker' in dns:
        data += bytes.fromhex(re.findall(REGEX, dns)[0])

with open('data.zip', 'wb') as f:
    f.write(data) # la flag è in data.zip -> dati sensibili -> gattoflag.png