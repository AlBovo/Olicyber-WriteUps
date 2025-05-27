#!/usr/bin/env python3

flag_enc = 522322238023102381231023652522102341238229023572002300237725721123462522002313213201235725725729023752902340233223302377280232023
flag_enc_test = 522316297286230237627329123232912316200237221023872622712361237123112312237227228325123212361236123402352295291239523223302377280232023

# livello 1 e livello 1 reversato
def liv_1(flag, flen):
    for i in range(flen):
        v3 = flag[i]
        v4 = 0
        if ord(v3) > 99:
            v4 = ord(v3) + 100
        else:
            v4 = ord(v3) - 20
        flag = flag[0:i] + chr(v4) + flag[i+len(chr(v4)):]
    return flag

def rev_liv_1(src, flen):
    for i in range(flen):
        v3 = src[i]
        v4 = 0
        if ord(v3) > 99:
            v4 = ord(v3) - 100
        else:
            v4 = ord(v3) + 20
        src = src[0:i] + chr(v4) + src[i+len(chr(v4)):]
    return src
    
# livello 2 e livello 2 reversato
def liv_2(flag, flen):
    v3, v4 = 0, 0
    v10 = ''
    for i in range(flen):
        s = str(ord(flag[i]))
        src = str(len(s))
        v10 += src
        v10 += s
    return v10

def rev_liv_2(src, flen):
    pos = 0
    flag, temp = "", ""
    while pos < flen:
        leng = int(src[pos])
        pos += 1
        flag += chr(int(src[pos:pos+leng]))
        # print(int(src[pos:pos+leng]))
        pos += leng
    return flag
    
# livello 3 e livello 3 reversato
def liv_3(flag, flen):
    src = ""
    for i in range(flen):
        src += flag[flen - i -1]
    return src

def rev_liv_3(src, flen):
    flag = " " * 520
    for i in range(flen):
        flag = flag[0:flen-i-1] + src[i] + flag[flen-i-1+len(src[i]):]
    flag = flag.strip()
    return flag
        
flag = "flag{OwO-https://youtu.be/dQw4w9WgXcQ}"
flag1 = liv_1(flag, len(flag))
flag2 = liv_2(flag1, len(flag1))
flag3 = liv_3(flag2, len(flag2))

assert int(flag3) == flag_enc_test

flag2_rev = rev_liv_3(flag3, len(flag3))
assert flag2_rev == flag2
flag1_rev = rev_liv_2(flag2_rev, len(flag2_rev))
assert flag1_rev == flag1
flag_dec = rev_liv_1(flag1_rev, len(flag1_rev))
assert flag_dec == flag

flag2_rev = rev_liv_3(str(flag_enc), len(str(flag_enc)))
flag1_rev = rev_liv_2(flag2_rev, len(flag2_rev))
flag_dec = rev_liv_1(flag1_rev, len(flag1_rev))
print(flag_dec)
