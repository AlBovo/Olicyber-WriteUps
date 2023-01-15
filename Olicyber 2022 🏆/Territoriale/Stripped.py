from pwn import *
b = False
prec = b""
with ELF("stripped") as file:
    s = file.data.find(b"flag")
    f = file.data[s:].find(b"}")
    print(file.data[s:s+f+1].decode())