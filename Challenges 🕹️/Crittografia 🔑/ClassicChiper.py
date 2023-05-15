alphabet = "abcdefghijklmnopqrstuvwxyz"

def key():
    for i in range(1, 26):
        yield "".join([alphabet[i:], alphabet[0:i]])

def decrypt(enc, key):
    plain = ""
    for k in range(len(enc)):
        character = enc[k]
        if ord(character) <= 122 and ord(character) >= 97:
            i = key.index(character)
            characterEncrypted = alphabet[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            plain = "".join([plain,characterEncrypted])
        else:
            plain = "".join([plain,character])
    return plain
    
for i in key():
    d = decrypt("xcqv{gvyavn_zvztv_etvtddlnxcgy}", i)
    if "flag" in d:
        print(d, end="")