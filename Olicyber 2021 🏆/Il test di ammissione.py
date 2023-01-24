from pwn import remote, context

def solve():
    f = ""
    c = 1
    for i in mosse:
        min = int(10e9)
        pos = 0
        for e in i:
            if min > stato[e]:
                min = stato[e]
                pos = e
        for e in i:
            stato[e] += 5-min
        for r in range(5-min):
            f += str(c) + " "
        c+=1
    return f
    
r = remote("test.challs.olicyber.it", 15004)
context.log_level = 'debug'
r.recvlines(20)

livello = r.recvline()
while livello.startswith(b"Livello"):
    stato = [int(_) for _ in r.recvline(False).decode().split()]
    mosse = []
    while True:
        s = r.recvline(False).decode()
        if s == "":
            break
        mosse.append(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(_) for _ in s.split()])
    res = solve()
    r.sendline(res)
    r.recvlines(2)
    livello = r.recvline()
