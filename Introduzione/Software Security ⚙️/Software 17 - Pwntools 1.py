from pwn import *
def somma(l):
    s = 0
    for i in l:
        s += int(i)
    return s

r = remote("software-17.challs.olicyber.it", 13000)
r.recvline()
r.sendline()
for _ in range(10):
    r.recvuntil(b"numeri\n")
    num = r.recvuntil(b"]").decode().replace("]","").replace("[","").split(", ")
    r.recv(100)
    r.sendline(str(somma(num)).encode())
print(r.recv(100))