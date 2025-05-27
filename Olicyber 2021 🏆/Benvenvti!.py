chip = "synt{Orairahgv_nyyn_pgs!}"
shift = ord(chip[0])-ord('f')
for i in chip:
    if i == '{' or i == '}' or i == '_' or i == '!':
        print(i, end="")
        continue
    if i.isupper():
        print(chr(((ord(i)+shift)-ord('A'))%26+ord('A')), end="")
    else:
        print(chr(((ord(i)+shift)-ord('a'))%26+ord('a')), end="")