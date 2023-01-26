from Crypto.Util.number import *
cipher = [6513402340379073542230710001434049959082564276254477896792619, 
          2739603094136133383923409703861575117091198809308633380325460]
n = 9565158649535229609530047362785645907094563351070470563788237
e = 65537
p = 2771826449193354891007108898387 # funzione factor(n) su sagemath
q = 3450850486082503930213321971551
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
for i in cipher:
    print(long_to_bytes(pow(i, d, n)).decode(), end="")