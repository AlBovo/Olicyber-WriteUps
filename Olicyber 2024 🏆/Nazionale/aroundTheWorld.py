#!/usr/bin/env python3
import os
from PIL import Image, ExifTags
import matplotlib.pyplot as plt
from itertools import groupby
from datetime import datetime

files = []

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        img = Image.open(file)
        exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
        x, y = exif['GPSInfo'][2], exif['GPSInfo'][4]
        x = int(x[0]) + int(x[1])/60 + int(x[2])/3600
        y = int(y[0]) + int(y[1])/60 + int(y[2])/3600
        date = datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        files.append((date.timestamp(), date.day, x, y))

# I had to copy this one cause who tf can guess this part
files.sort()
for _, file in groupby(files, key=lambda x: x[1]):
    file = list(file)
    print(file)
    plt.plot([f[3] for f in file], [f[2] for f in file], "-o")
plt.show()