#!/usr/bin/env python3
from sudoku import Sudoku

a = '500003080003040000780000090001200000000001960007000032000400500002009000090120006'
arr = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        arr[i][j] = int(a[i * 9 + j])

sudoku = Sudoku(3, 3, board=arr)
solve = sudoku.solve().board

indxs = [
    1,   2,   3,   4,   6,   8,   9,  10,  12,  14, 
   15,  16,  17,  20,  21,  22,  23,  24,  26,  27, 
   28,  31,  32,  33,  34,  35,  36,  37,  38,  39, 
   40,  44,  45,  46,  48,  49,  50,  51,  54,  55, 
   56,  58,  59,  61,  62,  63,  64,  66,  67,  69, 
   70,  71,  72,  74,  77,  78,  79
]

flag = 'flag{'
for i in indxs:
    flag += chr(solve[i // 9][i % 9] + ord('0'))
flag += '}'
print(flag)