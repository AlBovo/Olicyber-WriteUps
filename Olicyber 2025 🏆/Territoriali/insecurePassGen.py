import os
import string

flag = "fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-mare-fiume-strada-giorno-amico-vento-vento-mare-}".split('-')

words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola", 
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella", 
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

passphrase = []

for c in flag:
    if c in words:
        passphrase.append(chr(ord('a') + words.index(c)))
    else:
        passphrase.append(c)

print(''.join(passphrase))
