import http.client
from time import sleep
import random
array = ["61bb46", "fdb827", "f5821f", "e03a3e", "963d97", "009ddc"]
while True:
    
    for i in range(0,58):
        conn = http.client.HTTPConnection("192.168.0.15")    
        cmd1 = random.choice(array)
        strrequest = "/sec/?pt=35&ws={}&chip={}".format(cmd1, i)
        conn.request("GET", strrequest)
        sleep(0.5)

