dizionario_baconiano = {
    "00000":"A",
    "00001":"B",
    "00010":"C",
    "00011":"D",
    "00100":"E",
    "00101":"F",
    "00110":"G",
    "00111":"H",
    "01000":"I",
    "01001":"K",
    "01010":"L",
    "01011":"M",
    "01100":"N",
    "01101":"O",
    "01110":"P",
    "01111":"Q",
    "10000":"R",
    "10001":"S",
    "10010":"T",
    "10011":"U",
    "10100":"W",
    "10101":"X",
    "10110":"Y",
    "10111":"Z"
}
flag = open("ABcon.txt", "r").read().replace("A","1").replace("B","0").replace("\n","")
for i in flag.split(" "):
    if i == '{' or i == '_' or i == '}':
        print(i, end="")
    else:
        print(dizionario_baconiano[i], end="")