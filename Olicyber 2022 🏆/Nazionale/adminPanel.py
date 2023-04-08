from hashlib import sha256
import os
while True:
    rnd = os.urandom(8).hex().encode()
    txt = sha256(rnd).hexdigest()
    if txt[:6] == "bed100":
        print(rnd, txt)
# gli hash restituiti romperanno il check
# per admin panel 1 basta fare directory trasversal con ../../passwords nell'opzione 3