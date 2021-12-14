import requests as rq
from ping3 import ping

ServerUrl = ""

#Set Header
headers = {'User-Agent': 'ServerStatClient/1.0'}
#Get request to get external ip
pi = rq.get("http://ipv4.icanhazip.com").content.decode('utf8').rstrip("\n")
#Grouping the return 
def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True

#Print Note
print("\nPlz this is may not accurate or can make many problem")
#Building post data
if myping(pi) == False :
    data = {'Status':'Offline'}
else :
    data = {'Status':'Online'}

#Post it
session = rq.Session()
session.post(ServerUrl, headers=headers, data=data)
