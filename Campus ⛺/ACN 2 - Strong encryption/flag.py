def checkKey(key): # dato dal README.md
    if key < 0:
        return False
    if key > 25:
        return False
    if (key - 10) > 10 :
        return False
    a = (key * 257)
    key = key - 7  
    b = (key * 406) + 11  
    if a == b:
        return True
    return False

shift = 0
for i in range(26):
    if checkKey(i):
        print(i) # 19
        shift = i*-1
        break
plain = """Vbth, lhgh ikxhvvnitmt vax vb lmbtgh lvhikxgwh.
Lh vax be kxitkmh BM lmt etohktgwh lne ybex bg teexztmh ixk vtibkx vab x lmtmh be vheixohex.
Kbxlvb t vtibkx lx mkhoxktggh et ghlmkt x-ftbe x be ybex vax mb ah bgobtmh?

Itllphkw sbi: ynefbvhmhgx"""
for i in plain:
    if i in "abcdefghijklmnopqrstuvwxyz":
        print(chr(((ord(i)+shift)-ord('a'))%26+ord('a')), end="")
    elif i in "abcdefghijklmnopqrstuvwxyz".upper():
        print(chr(((ord(i)+shift)-ord('A'))%26+ord('A')), end="")
    elif i in "0123456789":
        print(chr(((ord(i)+shift)-ord('0'))%10+ord('0')), end="")
    else:
        print(i, end="")
''' La flag è quindi acn{fulmicotone} '''