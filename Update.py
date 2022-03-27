import requests as rq
from ping3 import ping

#https://github.com/JtuStuff/ServerStat-Client
ServerUrl = "YOUR URL TO UPDATE"

#Set Header
headers = {'User-Agent': 'ServerStatClient/1.0'}
#Get request to get external ip
pi = rq.get("http://ipv4.icanhazip.com").content.decode('utf8').rstrip("\n")
#Grouping the return 
pong = ping(pi)
if pong != None:
    data = {'Status':'Online'}
else:
    data = {'Status':'Offline'}

#Print Note
print("\nPlz this is may not accurate or can make many problem")
#Building post data

#Post it
session = rq.Session()
session.post(ServerUrl, headers=headers, data=data)
