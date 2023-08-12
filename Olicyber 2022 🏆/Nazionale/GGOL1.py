#!/usr/bin/env python3
from PIL import Image


class Critters:
    """Simplified implementation of https://en.wikipedia.org/wiki/Critters_(cellular_automaton)"""

    def __init__(self, grid):
        self.grid = grid
        self.h = len(grid) # altezza
        self.w = len(grid[0]) # lunghezza
        self.roundno = 0

        if self.h % 2 != 0 or self.w % 2 != 0:
            raise ValueError("The grid dimensions must be a multiple of two")
        if any(c not in (0, 1) for row in grid for c in row):
            raise ValueError("The grid must contain either 0 or 1")

    def step(self):
        self.roundno -= 1
        off = self.roundno % 2  # 0, 1, 0, 1, 0 ... 

        for j in range(0, self.h - 1, 2):
            for i in range(0, self.w - 1, 2):
                c00 = self.grid[(off + j) % self.h][(off + i) % self.w]
                c01 = self.grid[(off + j) % self.h][(off + i + 1) % self.w]
                c11 = self.grid[(off + j + 1) % self.h][(off + i + 1) % self.w]
                c10 = self.grid[(off + j + 1) % self.h][(off + i) % self.w]

                s = c00 + c10 + c01 + c11

                if s == 2:
                    pass
                elif s == 1:
                    c00, c01, c11, c10 = c01, c11, c10, c00
                    c00, c01, c11, c10 = c00 ^ 1, c01 ^ 1, c11 ^ 1, c10 ^ 1
                else:
                    c00, c01, c11, c10 = c00 ^ 1, c01 ^ 1, c11 ^ 1, c10 ^ 1

                self.grid[(off + j) % self.h][(off + i) % self.w] = c00
                self.grid[(off + j) % self.h][(off + i + 1) % self.w] = c01
                self.grid[(off + j + 1) % self.h][(off + i + 1) % self.w] = c11
                self.grid[(off + j + 1) % self.h][(off + i) % self.w] = c10


img_in = Image.open("flag.png").convert("L")

# convert black to 1 and white to 0
grid = [
    [1 if img_in.getpixel((i, j)) == 0 else 0 for i in range(img_in.width)]
    for j in range(img_in.height)
]

critters = Critters(grid)
for _ in range(42):
    critters.step()

# save the image
img_out = Image.new(mode="L", size=img_in.size)
img_out_px = img_out.load()
for i in range(img_in.width):
    for j in range(img_in.height):
        x = critters.grid[j][i]
        img_out_px[i, j] = 255 if x == 0 else 0

img_out.save(f"out.png")
