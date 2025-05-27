#!/usr/bin/env python3

from pwn import *
import re

r = remote("ihc.challs.olicyber.it", 34008)
r.recvuntil(b'invio!')
r.sendline()
t = r.recvuntil(b'Risposta: ').decode()
flag = ''

while not "}" in t.lower():	
	f = re.search(r':\s(.)(?=\n)', t)
	if f:
		flag += f.group(1)
		print(flag)
		if f.group(1) == '}':
			exit(0)
	if "Quante volte compare" in t:
		l = re.search(r'lettera\s(.+?)\snella', t).group(1)
		s = re.search(r'stringa\s(.+)', t).group(1)
		print(f'("query":0, "lettera":"{l}", "stringa":"{s}")')
		r.sendline(str(s.count(l)).encode())
	elif "stringa al contrario" in t:
		s = re.search(r':\s(.+)', t).group(1)
		print(f'("query":1, "stringa":"{s}")')
		r.sendline(s[::-1].encode())
	elif "nelle posizioni" in t:
		array = eval("[" + re.search(r'\[(.*?)\]', t).group(1) + "]")
		s = re.search(r'stringa\s(.+)', t).group(1)
		print(f'("query":2, "array":"{str(array)}", "stringa":"{s}")')
		f = ''
		for i in array:
			f += s[i-1] 
		r.sendline(f.encode())
	elif "Qual è il risultato" in t:
		exp = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', t).group(1)
		print(f'("query":3, "exp":"{exp}")')
		r.sendline(str(int(eval(exp))).encode())
	else:
		print(t)
		exit(0)
	t = r.recvuntil(b'Risposta: ').decode()
print(flag + '}')
