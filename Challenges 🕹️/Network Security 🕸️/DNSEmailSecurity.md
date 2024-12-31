# Soluzione
Per verificare la sicurezza di un indirizzo email si possono usare due record: DKIM e SPF.
Nel caso di questa challenge scrivendo questo comando (derivato da quello dato dalla challenge stessa)
```
dig -p10502 @emailsec.challs.olicyber.it _spf.dns-email.localhost TXT
```
E' possibile ottenere la risposta 
```
; <<>> DiG 9.20.4 <<>> -p10502 @emailsec.challs.olicyber.it _spf.dns-email.localhost TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 14427
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;_spf.dns-email.localhost.	IN	TXT

;; ANSWER SECTION:
_spf.dns-email.localhost. 3600	IN	TXT	"v=spf1 redirect=_spf.mail.dns-email.localhost."

;; Query time: 173 msec
;; SERVER: 5.75.221.48#10502(emailsec.challs.olicyber.it) (UDP)
;; WHEN: Tue Dec 31 16:34:30 CET 2024
;; MSG SIZE  rcvd: 125
```
A questo punto basta rifare il comandando seguendo il redirect a `_spf.mail.dns-email.localhost` per trovare l'ultimo dominio
```
; <<>> DiG 9.20.4 <<>> -p10502 @emailsec.challs.olicyber.it _spf.mail.dns-email.localhost TXT
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10278
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;_spf.mail.dns-email.localhost.	IN	TXT

;; ANSWER SECTION:
_spf.mail.dns-email.localhost. 3600 IN	TXT	"v=spf1 include:_netblocks.mail.dns-email.localhost."

;; Query time: 150 msec
;; SERVER: 5.75.221.48#10502(emailsec.challs.olicyber.it) (UDP)
;; WHEN: Tue Dec 31 16:34:42 CET 2024
;; MSG SIZE  rcvd: 140
```
A questo punto facendo una richiesta al DNS senza specificare nessun record si troverà la flag nel CNAME del dominio `_netblocks.mail.dns-email.localhost`

```
; <<>> DiG 9.20.4 <<>> -p10502 @emailsec.challs.olicyber.it _netblocks.mail.dns-email.localhost
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44303
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;_netblocks.mail.dns-email.localhost. IN	A

;; ANSWER SECTION:
_netblocks.mail.dns-email.localhost. 3600 IN CNAME flag{dNs_15_fuLl_0f_qu35t!On5}.dns-email.localhost.

;; Query time: 170 msec
;; SERVER: 5.75.221.48#10502(emailsec.challs.olicyber.it) (UDP)
;; WHEN: Tue Dec 31 16:35:44 CET 2024
;; MSG SIZE  rcvd: 152
```