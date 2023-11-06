#!/usr/bin/env python3

f0 = 74
f1 = 27971424
f2 = 75
f3 = 65537

flag = bytes.fromhex("1022179cd41e2bd156c393830b79ef960a007155f79d368290ad582e7f954deb1c91c03d07705ca964a3")

for i in range(len(flag)):
    f1 = ((f0 + f1 * f2) % f3)
    print(chr((f1 % 256) ^ flag[i]), end="")

print()