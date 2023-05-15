flag = "cixd{xsb_zxbpxo_jlofqrof_qb_pxirqxkq}"
shift = ord('f') - ord('c')
for i in flag:
    if i == '{' or i == '}' or i == '_':
        print(i, end="")
        continue
    else:
        print(chr(((ord(i)+shift)-ord('a'))%26+ord('a')), end="")