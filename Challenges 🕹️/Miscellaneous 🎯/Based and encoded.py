import socket, binascii, base64
s = socket.socket()
s.connect(("based.challs.olicyber.it", 10600)) # ancora in beta
r = s.recv(1000).decode()
while "flag" not in r.lower():
    if "binario" in r.lower():
        if "in" in r.lower():
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    resp = ""
                    for i in map(bin,bytearray(line["message"].encode())):
                        resp += i.replace("0b", "")
                    d = {"answer":f"{resp}"}
                    s.send(d)
        else:
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    res = line["mesasage"]
                    resp = ''.join([ chr(int(res[i:i+8],2)) for i in range(0,len(res),8)])
                    d = {"answer":f"{resp}"}
                    s.send(d)
    elif "esadecimale" in r.lower():
        if "in" in r.lower():
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    resp = binascii.hexlify(line["message"].encode()).decode()
                    d = {"answer":f"{resp}"}
                    s.send(d)
        else:
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    resp = bytes.fromhex(line["mesasage"].encode()).decode()
                    d = {"answer":f"{resp}"}
                    s.send(d)
    elif "base64" in r.lower():
        if "in" in r.lower():
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    resp = base64.b64encode(line["mesasage"].encode())
                    d = {"answer":f"{resp}"}
                    s.send(d)
        else:
            for line in r.split("\n"):
                if type(line) == dict:
                    print(line)
                    resp = base64.b64decode(line["mesasage"].encode())
                    d = {"answer":f"{resp}"}
                    s.send(d)
    r = s.recv(1000).decode()

print(r)