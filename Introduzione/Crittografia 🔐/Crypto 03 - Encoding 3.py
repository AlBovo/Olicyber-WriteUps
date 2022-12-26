import base64
flag1 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE=" # prima parte della flag
flag2 = 664813035583918006462745898431981286737635929725 # seconda parte della flag
print((base64.b64decode(flag1) + flag2.to_bytes(20, 'big')).decode("ascii")) # decripto e printo l'intera flag
''' La flag di questa chall è: flag{w41t_1ts_all_b1ts?_4lw4ys_H4s_b33n} '''