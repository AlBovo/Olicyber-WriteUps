from functools import cache

MASK = 2**64-1

@cache
def serie(a):
    if a == 0:
        return a
    elif a == 1:
        return a
    return ((3 * serie(a-1) & MASK)-(2*serie(a-2) & MASK)) & MASK

for i in range(10000000):
    b = serie(i)
print(hex(serie(1000000)))
# basta poi saltare serie settando il parametro a 0 (registro rdi)
# e poi impostare il registro rdi di print_flag a 0xff....
