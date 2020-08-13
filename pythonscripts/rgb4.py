import http.client
from time import sleep
import random
array = ["61bb46", "fdb827", "f5821f", "e03a3e", "963d97", "009ddc"]
while True:
    cmd1 = ''
    for i in range(0,58):
        cmd1 += random.choice(array) 
        
    conn = http.client.HTTPConnection("192.168.0.15")
    strrequest = "/sec/?pt=35&ws={}".format(cmd1,)
    conn.request("GET", strrequest)
    sleep(1)
