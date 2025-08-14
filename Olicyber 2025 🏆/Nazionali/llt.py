#!/usr/bin/env python3
import pyshark
import re

REGEX = r'flag{.*}'
capture = pyshark.FileCapture(
    "llt.pcap",
    display_filter='ip.dst == 172.67.157.96'
)

ttl_values = []
for packet in capture:
    try:
        ttl = int(packet.ip.ttl)
        ttl_values.append(ttl)
    except AttributeError:
        pass
capture.close()

flag = ''.join([chr(i) for i in ttl_values])
print(re.findall(REGEX, flag)[0])
