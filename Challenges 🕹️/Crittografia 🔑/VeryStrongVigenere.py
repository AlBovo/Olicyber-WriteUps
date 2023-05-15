flag = "fzau{ncn_isors_cviovw_pwcqoze}"
flag1 = "flag"
d = [0, 0, 0, 0]
for i in range(4):
    d[i] = abs(ord(flag[i])-ord(flag1[i]))
flag1 = ""
print(d) # si nota che la chiave si ripete 0,14 ed è quindi formata da due caratteri
b = True
for i in flag:
    if i == '{' or i == '}' or i == '_':
        flag1 += i
    elif b:
        flag1 += i # lo shift è di 0
        b = False
    else:
        flag1 += chr((ord(i)-ord('a')-14) % 26 + ord('a')) # lo shift è di 14
        b = True
print(flag1)