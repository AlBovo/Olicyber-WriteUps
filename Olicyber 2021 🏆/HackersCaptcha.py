#!/usr/bin/env python3
from pwn import *

r = remote('hcaptcha.challs.olicyber.it', 20007)
r.recvline()
r.recvline()

nums = [
    [
        r'_______   ',
        r'\   _  \  ',
        r'/  /_\  \ ',
        '\\  \\_/   \\',
        r' \_____  /',
        r'       \/ '
    ],
    [
        r' ____ ',
        r'/_   |',
        r' |   |',
        r' |   |',
        r' |___|',
        r'      '
    ],
    [
        r'________  ',
        r'\_____  \ ',
        r' /  ____/ ',
        r'/       \ ',
        '\\_______ \\',
        r'        \/'
    ],
    [
        r'________  ',
        r'\_____  \ ',
        r'  _(__  < ',
        ' /       \\',
        r'/______  /',
        r'       \/ '
    ],
    [
        r'   _____  ',
        r'  /  |  | ',
        r' /   |  |_',
        r'/    ^   /',
        r'\____   | ',
        r'     |__| '
    ],
    [
        r' .________',
        r' |   ____/',
        r' |____  \ ',
         ' /       \\',
        r'/______  /',
        r'       \/ '
    ],
    [
        r'  ________',
        r' /  _____/',
        r'/   __  \ ',
        '\\  |__\\  \\',
        r' \_____  /',
        r'       \/ '
    ],
    [
        r'_________ ',
        '\\______  \\',
        r'    /    /',
        r'   /    / ',
        r'  /____/  ',
        r'          '
    ],
    [
        r'  ______  ',
        r' /  __  \ ',
        r' >      < ',
        '/   --   \\',
        r'\______  /',
        r'       \/ '
    ],
    [
        r' ________ ',
        '/   __   \\',
        r'\____    /',
        r'   /    / ',
        r'  /____/  ',
        r'          '
    ]
]

signs = [
    [
        r'         ',
        r' /\|\/\  ',
        r'_)    (__',
        r'\_     _/',
        r'  )    \ ',
        r'  \/\|\/ '
    ],
    [
        r'       ',
        r'       ',
        r' ______',
        r'/_____/',
        r'       ',
        r'       '
    ],
    [
        r'          ',
        r'   .__    ',
        r' __|  |___',
        r'/__    __/',
        r'   |__|   ',
        r'          '
    ],
    [
        r'       ',
        r' ______',
        r'/_____/',
        r'/_____/',
        r'       ',
        r'       ',
    ]
]
signsn = ['*', '-', '+', '=']

for _ in range(100):
    f = [r.recvline().decode()[:-1] for _ in range(6)]
    eq = ""
    print(_)
    while True:
        flag = False
        for num in nums:
            if all(f[i].startswith(num[i]) for i in range(6)):
                eq += str(nums.index(num))
                f = [f[i][len(num[i])+1:] for i in range(6)]
                flag = True
                break
        if flag:
            continue
        for sign in signs:
            if all(f[i].startswith(sign[i]) for i in range(6)):
                eq += signsn[signs.index(sign)]
                f = [f[i][len(sign[i])+1:] for i in range(6)]
                flag = True
                break
        if not flag:
            print("Error")
            exit(0)
        if eq[-1] == '=':
            eq = eq[:-1]
            break
    
    r.recvuntil(b': ')
    r.sendline(str(eval(eq)).encode())
r.interactive()