#!/usr/bin/env python3
import pyshark

cap = pyshark.FileCapture('capture.pcapng', display_filter='tcp.stream eq 36') # found with wireshark

flag = ""
for i in cap:
    try:
        flag += str(i.data.data.binary_value.decode('utf-8'))
    except:
        continue
flag = flag.replace('\n','')
flag = flag[flag.index('fmcj{'):flag.index('}')+1]
# print(flag) fmcj{yo_ackyzb_ihruvcvjam}
f = [""]*len(flag)
t = 0
for i in range(len(flag)):
    if flag[i] == '{' or flag[i] == '}' or flag[i] == '_':
        f[i] = flag[i]
    else:
        f[i] = chr((ord(flag[i])-i - ord('a'))%26 + ord('a'))
    # print(t)
print("".join(f))