from pwn import *
r = remote("ihc.challs.olicyber.it", 34008)
r.recv(1000)
r.sendline()
while True:
    f = r.recv(1000).decode("utf-8")
    print(f)
    if "flag" in f:
        print(f)
        exit(0)
    if "lettere nelle pos" in f:
        lista = eval(f[f.find("["):f.find("]")+1])
        stringa = f[f.find("nella stringa") + len("nella stringa "):f.find("?")+1]
        for i in lista:
            print(stringa[i-1], end=" ")
    elif "contrario" in f:
        stringa = f[f.find(": ")+2:f.find("\n")]
        print(stringa[::-1])
    elif "volte compare" in f:
        lettera = f[f.find("lettera ")+len("lettera ")]