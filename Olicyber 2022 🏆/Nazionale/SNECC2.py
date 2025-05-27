#!/usr/bin/env python3
from pwn import remote
import pyshark, json, OpenSSL

cap = pyshark.FileCapture('traffic.pcap', display_filter='tcp')

def xor(a, b):
    return bytes([a[i]^b[i%len(b)] for i in range(len(a))])

def cert_gen( # https://stackoverflow.com/questions/27164354/create-a-self-signed-x509-certificate-in-python
    emailAddress="emailAddress",
    commonName="commonName",
    countryName="NT",
    localityName="localityName",
    stateOrProvinceName="stateOrProvinceName",
    organizationName="organizationName",
    organizationUnitName="organizationUnitName",
    serialNumber=0,
    validityEndInSeconds=10*365*24*60*60):

    k = OpenSSL.crypto.PKey()
    k.generate_key(OpenSSL.crypto.TYPE_RSA, 4096)
    cert = OpenSSL.crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName
    cert.get_subject().OU = organizationUnitName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    return OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

def connect(key):
    try:
        jsonFile = open('traffic.json', 'r')
        d = json.load(jsonFile)
        jsonFile.close()
        return d[str(key)]
    except FileNotFoundError as e:
        jsonFile = open('traffic.json', 'w')
        d = {}
        last = 'Bye'
        int1, int2 = 0, 0
        for pkt in cap:
            try:
                data = bytes.fromhex(pkt.data.data).decode().strip()
                if last == 'Bye' or last == 'No':
                    int1 = int(data)
                    last += '00'
                    continue
                if last == 'Bye00' or last == 'No00':
                    int2 = int(data)
                if int1 != 0 and int2 != 0 and data == 'Bye':
                    d[int1] = int2
                    print('Bye', int1, int2)
                    int1, int2 = 0, 0
                elif data == 'No':
                    print('No', int1, int2)
                    int1, int2 = 0, 0
                # print(data)
                last = data
            except AttributeError as e:
                pass
            
        jsonFile.write(json.dumps(d))
        connect(key)

r = remote("snecc.challs.olicyber.it", 12310)
key = r.recvline().decode().strip()
r.sendline(str(connect(key)).encode())
# r.interactive()
r.recvuntil(b'> ')
r.sendline(b'2')
data = bytes.fromhex(r.recvline().decode().strip())
k = b"G_ab!bb_oR_oss_o"
messaggio_segreto = xor(data, k)
# print(messaggio_segreto.decode())
r.recvuntil(b'> ')
cert = xor(cert_gen(commonName='1337.olicyber'), k).hex()
r.sendline(cert.encode())
risp = xor(bytes.fromhex(r.recvline().strip().decode()), k).decode()
print(risp)
r.close()