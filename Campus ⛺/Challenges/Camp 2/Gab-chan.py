#!/usr/bin/env python3

import os

os.system("stegolsb steglsb -r -i Gab-chan.png -o file.zip") # pip install stego-lsb
os.system('unzip -P "VjyQ[6M8WFx[sLCT" file.zip') # unzippo
with open("flag.txt", "r") as flag:
    print(flag.read()) # printo la flag
