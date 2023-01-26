from pwn import *
HOST = 'software-18.challs.olicyber.it'
PORT = 13001

conn = remote(HOST, PORT)

conn.recv(100)
conn.send(b"s\n")

for _ in range(100):
    try:
        conn.recvuntil(b"0x")
    except:
        print(f)
        print(num)
        conn.interactive()
    num = conn.recvuntil(b" ").decode().strip()
    f = conn.recv(100)
    if b"unpacked" in f and b"64" in f:
        conn.sendline(u64(num))
        print("u64")
    elif b"unpacked" in f and b"32" in f:
        conn.sendline(u32(num))
        print("u32")
    elif b"packed" in f and b"64" in f:
        conn.sendline(p64(int(num, 16), endianness='little'))
        print("p64")
    elif b"packed" in f and b"32" in f:
        conn.sendline(p32(int(num, 16), endianness="little"))
        print("p32")
print(conn.recv(100).decode())