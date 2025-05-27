#!/usr/bin/env python3

from pwn import *
from base64 import b64decode, b64encode
import re

r = remote("based.challs.olicyber.it", 10600)
r.recvuntil(b'\n\n')

def bin_to_str(x):
    ''' Copiata lol '''
    my_int = int(x, base=2)
    my_str = my_int.to_bytes((my_int.bit_length() + 7)//8, 'big')
    return my_str

while True:
	t = r.recv(1000).decode()
	print(t)
	if 'da base64' in t:
		t = t.split('\n')
		j = eval(t[1])
		r.sendline(b'{"answer": "' +  b64decode(j["message"].encode()) + b'"}')
	elif 'da esadecimale' in t:
		t = t.split('\n')
		j = eval(t[1])
		r.sendline(b'{"answer": "' + bytes.fromhex(j["message"]) + b'"}')
	elif 'da binario' in t:
		t = t.split('\n')
		j = eval(t[1])
		r.sendline(b'{"answer": "' + bin_to_str("0b"+j["message"]) + b'"}')
	elif 'a base64' in t:
		t = t.split('\n')
		j = eval(t[1])
		r.sendline(b'{"answer": "' + b64encode(j["message"].encode()) + b'"}')
	elif 'a esadecimale' in t:
		t = t.split('\n')
		j = eval(t[1])
		r.sendline(b'{"answer": "' + j["message"].encode().hex().encode() + b'"}')
	elif 'a binario' in t:
		t = t.split('\n')
		j = eval(t[1])
		binstr = ''.join(format(ord(i), '08b') for i in j["message"])
		if binstr[0] != '1':
			for i in range(len(binstr)):
				if binstr[i] == '1':
					binstr = binstr[i:]
					break
		r.sendline(b'{"answer": "' +  binstr.encode() + b'"}')
	else:
		print("skill issue", t)
	flag = r.recvuntil(b'\n\n')
	if b'flag' in flag.lower():
		print(flag)
		break
	
