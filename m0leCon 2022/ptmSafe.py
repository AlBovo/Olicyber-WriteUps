#!/usr/bin/env python3

flag = [b''] * 16

flag[0] = b'p'
flag[1] = b't'
flag[2] = b'm'
flag[3] = b'{'

flag[4] = chr(ord('p') ^ 0x1e).encode()
flag[5] = b'0'
flag[6] = chr((3 * ord(flag[4].decode())) ^ 318).encode()
flag[7] = b'_'
flag[9] = chr(int(pow(110592, 1/3)) + 1).encode()
flag[12] = chr(208//4).encode()
flag[13] = b'f'
flag[8] = chr(ord(flag[12].decode()) ^ 71).encode()
flag[11] = chr(13225 // ord(flag[8].decode())).encode()
flag[10] = chr(ord(flag[4].decode()) + 100 - ord(flag[11].decode())).encode()
flag[14] = b'3'
flag[15] = b'}'

print(''.join([x.decode() for x in flag]))