import http.client
from time import sleep
import random
array = ["500000", "005000", "000050", "505050", "000000"]
while True:
    conn = http.client.HTTPConnection("192.168.0.15")
    cmd1 = random.choice(array)
    cmd2 = random.choice(array)
    cmd3 = random.choice(array)
    cmd4 = random.choice(array)
    cmd5 = random.choice(array)
    cmd6 = random.choice(array)
    strrequest = "/sec/?pt=35&ws={}{}{}{}{}{}".format(cmd1,cmd2,cmd3,cmd4,cmd5,cmd6)
    conn.request("GET", strrequest)
    sleep(1)