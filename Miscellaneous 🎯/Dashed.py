from base64 import b64decode
dizionario_morse = {'A':'.-', 'B':'-...', # template trovabile ovunque
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

flag = str(open("dashed.txt", "r").read()).split(" ")
temp_string = ""
for words in flag:
    for i in dizionario_morse:
        if dizionario_morse[i] == words:
            temp_string += i
temp_string = temp_string.replace("0X", "").replace(",", "").split(" ")
flag2 = ""
for numbers in temp_string:
    flag2 += bytes.fromhex(numbers).decode("ascii")
flag3 = int(flag2, 2).to_bytes(((flag2.__len__()) + 7) // 8, 'big').decode("ascii")
flag4 = b64decode(flag3).decode()
shift = -1
for i in flag4:
    if shift == -1:
        shift = ord(i) - ord('F')
    if i != '{' and i != '}' and i != '_':
        pos = ord(i) - ord('A')
        new_pos = (pos - shift) % 26
        print(chr(new_pos + ord('A')), end="")
    else:
        print(i, end="")
        
# TODO finire qua