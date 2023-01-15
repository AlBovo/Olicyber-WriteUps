# pip3 install pwntools
from pwn import remote, context
import re

r = remote("2048.challs.olicyber.it", 10007)
context.timeout = 1
sos = r.recv()
context.log_level = 'debug'

for i in range(2049):
    print(str(sos))
    if "DIVISIONE_INTERA" in str(sos):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(sos))]
        t = s[0] // s[1]
        r.sendline(str(t))
    elif "SOMMA" in str(sos):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(sos))]
        t = sum(s)
        r.sendline(str(t))
    elif "DIFFERENZA" in str(sos):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(sos))]
        t = s[0] - s[1]
        r.sendline(str(t))
    elif "PRODOTTO" in str(sos):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(sos))]
        t = s[0] * s[1]
        r.sendline(str(t))
    elif "POTENZA" in str(sos):
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(sos))]
        t = s[0] ** s[1]
        r.sendline(str(t))
    sos = r.recv()    
print(str(sos))