import http.client
from time import sleep
import random

# retrieve String item
# r = requests.get('http://192.168.0.6:8080/rest/items/itemPHP4/state')
# data = r.content
# print(data)

r = http.client.HTTPConnection("192.168.0.6:8080")
strrequest = "/rest/items/itemPHP4/state"
r.request("GET", strrequest)
response = r.getresponse()
print(type(response.read()))
print(type(response.read().decode("utf-8")))


array = ["61bb46", "fdb827", "f5821f", "e03a3e", "963d97", "009ddc"]
while response.read().decode("utf-8") == 'ON':
    cmd1 = ''
    for i in range(0,58):
        cmd1 += random.choice(array) 
        
    conn = http.client.HTTPConnection("192.168.0.15")
    strrequest = "/sec/?pt=35&ws={}".format(cmd1,)
    conn.request("GET", strrequest)
    sleep(1)
