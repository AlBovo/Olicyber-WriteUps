#!/usr/bin/env python3

from base64 import b64decode
import zipfile, os

data = b64decode("""UEsDBAoAAAAAADulm1QAAAAAAAAAAAAAAAAFABwAZGF0aS9VVAkAA3GOaWJyjmlidXgLAAEE
6AMAAAToAwAAUEsDBAoACQAAAMikm1Rtav/dPwAAADMAAAANABwAZGF0aS9mbGFnLnR4dFVU
CQADl41pYpeNaWJ1eAsAAQToAwAABOgDAADqjURVPEQmTgYftinWcYp1R87NwCw+inMGmSJx
Ndf3SFn9rf7VTQXPUfa4qogymeZk/HP9so/1hEOXvUosP7NQSwcIbWr/3T8AAAAzAAAAUEsB
Ah4DCgAAAAAAO6WbVAAAAAAAAAAAAAAAAAUAGAAAAAAAAAAQAP1BAAAAAGRhdGkvVVQFAANx
jmlidXgLAAEE6AMAAAToAwAAUEsBAh4DCgAJAAAAyKSbVG1q/90/AAAAMwAAAA0AGAAAAAAA
AQAAALSBPwAAAGRhdGkvZmxhZy50eHRVVAUAA5eNaWJ1eAsAAQToAwAABOgDAABQSwUGAAAA
AAIAAgCeAAAA1QAAAAAA""")
with open("file.zip", "wb") as file:
    file.write(data)

with zipfile.ZipFile("file.zip", "r") as file:
    file.extractall('./', pwd=b'cGX!#XpgRoi25v9m')
os.chdir("dati")
print(open("flag.txt", "r").read())
os.chdir("..")
os.system("rm -rf dati")
os.system("rm file.zip")

