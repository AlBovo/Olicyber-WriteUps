from pwn import *

conn = remote("crypto-08.challs.olicyber.it", 30001)
conn.recvuntil(b"\n\n")
f = conn.recvuntil(b"=").decode().replace(" =", "").split(" ")
t = []
for i in f:
    if i != '%':
        t.append(int(i))
conn.recv(1000)
conn.sendline(f"{t[0]%t[1]}".encode())
conn.recv(1000)
conn.recvuntil(b"\n\n")
f = conn.recvuntil(b"?").decode().replace("mod", "%").replace("(","").replace(")","").replace("?","").replace("== ","")
f = f.split(" ")
conn.recv(1000)
if int(f[0]) == int(f[1])%int(f[3]):
    conn.sendline(b"si")
else:
    conn.sendline(b"no")
conn.recvuntil(b"\n\n")
print(conn.recv(1000))

