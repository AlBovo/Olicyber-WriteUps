from Crypto.Util.Padding import unpad

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def add(a, b):
    return int.to_bytes((int.from_bytes(a, 'big') + int.from_bytes(b, 'big')) & ((1 << 128) - 1), 16, 'big')

def subtract(a, b):
    return int.to_bytes((int.from_bytes(a, 'big') - int.from_bytes(b, 'big')) & ((1 << 128) - 1), 16, 'big')

def rol(x, n):
    return int.to_bytes(((int.from_bytes(x, 'big') << n) | (int.from_bytes(x, 'big') >> (128 - n))) & ((1 << 128) - 1), 16, 'big')

def ror(x, n):
    return rol(x, 128 - n)

def prng(n, seed, iterations):
    numbers = []
    for _ in range(iterations):
        seed = (seed ** 2) % n
        numbers.append(seed)
    return numbers

def decrypt_block(key, block):
    assert len(key) == 32
    assert len(block) == 32
    k2, k1 = key[:16], key[16:32]
    b1, b2 = block[:16], block[16:]
    for r in range(ROUNDS - 1, -1, -1):
        b1 = xor(b1, k1)
        b1 = rol(b1, 31)
        b2 = xor(b2, k2)
        b2 = subtract(b2, b1)
    return b1 + b2

ROUNDS = 10
n = 28087460813174486059034414551240249788023923756050759856308458322681826441049323969972913966894664237696959566808290405727732350393345948504891177099061573610135163058514828369697643042666005384521714256517991315882984306833419862539867692692716617074207808746659453884745255262698130584357835902471931699817647567728572688737596486809390298684489842424609146835280833441401592250553573771844222020121038815882223862298294665424093073182955018154044019485219838690648719703150807518955331895641688078886409605207252562543480484708396495057837290115243183136250323437141077720724973892227190571167633700090224634792701
encrypted_flag = bytes.fromhex("f12d1653bd9d4c3196860b77ffbe1862c67aca872cf2f793b97678f2478c6b7a9859372ac514d815a28a2657060b64777a272ef12c2c670f908266e4df0e8243")

for seed in range(1000000):
    final_seed = prng(n, seed, 10)[-1]
    
    key_int = final_seed
    key_bytes = int.to_bytes(key_int, 2048 // 8, 'big')
    key = key_bytes[16:16 + 32]
    
    decrypted = b''
    for i in range(0, len(encrypted_flag), 32):
        ciphertext_block = encrypted_flag[i:i + 32]
        plaintext_block = decrypt_block(key, ciphertext_block)
        decrypted += plaintext_block
    
    try:
        plaintext = unpad(decrypted, 32)
        if plaintext.startswith(b'flag{') and plaintext.endswith(b'}'):
            print(f"Found the flag with seed {seed}:")
            print(plaintext.decode())
            break
    except ValueError:
        continue