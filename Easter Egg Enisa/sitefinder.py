import requests, string
import itertools
for i in string.ascii_lowercase:
    f = "cllaz" + i
    for e in itertools.permutations(f, 6):
        try:
            r = requests.get(f"http://{e[0]+e[1]+e[2]+e[3]+e[4]+e[5]}.online")
            print(f"http://{e[0]+e[1]+e[2]+e[3]+e[4]+e[5]}.online")
            print(r.status_code)
        except:
            continue