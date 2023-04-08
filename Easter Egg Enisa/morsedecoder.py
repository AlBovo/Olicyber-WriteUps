from PIL import Image
foto = Image.open("easter_eggs.png")
for i in range(128):
    r = foto.getpixel((i, 0))[0]
    g = foto.getpixel((i, 0))[1]
    b = foto.getpixel((i, 0))[2]
    print(chr(b) , end="")
    