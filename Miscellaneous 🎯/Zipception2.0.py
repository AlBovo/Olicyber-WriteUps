from zipfile import ZipFile
import os
# consiglio di usare la wordlist rockyou per craccare le password
# rockyou.txt è nella cartella /Wordlists

def crack_password(password_list, obj):
	idx = 0
	with open(password_list, "rb") as file:
		for line in file:
			for word in line.split():
				try:
					idx += 1
					obj.extractall(pwd=word)
					print("La password è: ", word.decode())
					return True
				except:
					continue
	return False
wordlist = open("rockyou.txt", "rb")
cnt = len(list(wordlist))
for i in range(100):
    obj = ZipFile(f"{100-i}.zip")
    if crack_password("rockyou.txt", obj) == False:
        print("La wordlist non contiene la password corretta")
        break
    obj.close()
    os.remove(f"{100-i}.zip")
# la flag sarà nel file flag.txt