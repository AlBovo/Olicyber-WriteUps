import pwn
print(pwn.connect("based.challs.olicyber.it", 10600).recvall().decode("ascii"))