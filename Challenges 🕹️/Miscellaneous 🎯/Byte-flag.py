with open("flag.png", "rb") as flag: # la foto deve essere nella main dir (Olicyber-WritesUp/....)
    text = flag.read()
    index = text.find("flag".encode())
    for i in range(index, len(text)):
        print(chr(text[i]), end="")