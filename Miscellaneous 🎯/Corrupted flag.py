from PIL import ImageSequence, Image
corrupted = open("corrupted_file", "rb").read()
notcorr = open("flag.gif", "wb")
print(corrupted[:13]) # magic number sbagliati
notcorr.write(b"GIF89a" + corrupted[13:])
notcorr.close()
notcorr = Image.open("flag.gif")
i = 0
for frame in ImageSequence.Iterator(notcorr):
    i += 1
    frame.save("frame-"+str(i)+".webp",format = "WebP", lossless = True)
# la flag la si trova fra i frame salvati