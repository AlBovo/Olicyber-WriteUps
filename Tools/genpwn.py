#!/usr/bin/env python3
import os, sys

template = '''
#!/usr/bin/env python3
from pwn import *

context.terminal = ('kgx', '-e')
context.binary = elf = ELF('./{}')
if args.REMOTE:
    r = remote('{}', {})
else:
    if args.LOCAL:
        r = process(elf.path)
    else:
        r = gdb.debug(elf.path, \'\'\'
            break *main
            continue
        \'\'\')
r.interactive()
'''[1:-1]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: genpwn <filename> <remote> <port>')
        sys.exit(1)
    filename = sys.argv[1]
    remote = sys.argv[2]
    port = sys.argv[3]

    t = template.format(filename, remote, port)
    with open('sol.py', 'w') as f:
        f.write(t)
    os.system('chmod +x sol.py')
    print('Generated sol.py')