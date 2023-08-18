#!/usr/bin/env python3
from pwn import remote
import pyshark, json

cap = pyshark.FileCapture('traffic.pcap', display_filter='tcp')

def connect(key):
    try:
        jsonFile = open('traffic.json', 'r')
        d = json.load(jsonFile)
        jsonFile.close()
        return d[str(key)]
    except FileNotFoundError as e:
        jsonFile = open('traffic.json', 'w')
        d = {}
        last = 'Bye'
        int1, int2 = 0, 0
        for pkt in cap:
            try:
                data = bytes.fromhex(pkt.data.data).decode().strip()
                if last == 'Bye' or last == 'No':
                    int1 = int(data)
                    last += '00'
                    continue
                if last == 'Bye00' or last == 'No00':
                    int2 = int(data)
                if int1 != 0 and int2 != 0 and data == 'Bye':
                    d[int1] = int2
                    print('Bye', int1, int2)
                    int1, int2 = 0, 0
                elif data == 'No':
                    print('No', int1, int2)
                    int1, int2 = 0, 0
                # print(data)
                last = data
            except AttributeError as e:
                pass
            
        jsonFile.write(json.dumps(d))
        connect(key)

r = remote("snecc.challs.olicyber.it", 12310)
key = r.recvline().decode().strip()
r.sendline(str(connect(key)).encode())
# r.interactive()
r.recvuntil(b'> ')
r.sendline(b'3')
print(r.recvline().decode().strip())