import time
import json
import ujson
import numpy.random as random
import math
import matplotlib.pyplot as plt

#Pour determiner le maximum de requetes en 1s:

###########################

rands = [[random.uniform(45.73, 45.84),random.uniform(4.680, 4.830),str(33600000000 + random.randint(0,199999999))] for i in range(1000)]

######################################
num_loops = 500

start = time.time()
for _ in range(num_loops):
    for randuple in rands:
        data = ujson.dumps({
            "data": {
                "latitude": randuple[0], "longitude": randuple[1], "timestamp": time.time()
            },
            "metadata": {
                "msisdn": randuple[2],
                "radius": 150
            }
        })
end = time.time()
print "La production de " + str(num_loops*1000) + " requetes a pris " + str(end - start) + " secondes"


############################################################################################################

#Pour tracer les performances en fonction du temps:

log_requests=[]
requests=[]
times=[]

for i in [1,3,10,30,100,300,1000,3000,10000]:
    start = time.time()
    for _ in range(i):
        for randuple in rands:
            data = ujson.dumps({
                "data": {
                    "latitude": randuple[0], "longitude": randuple[1], "timestamp": time.time()
                },
                "metadata": {
                    "msisdn": randuple[2],
                    "radius": 150
                }
            })
    end = time.time()

    times = times + [end-start]
    log_requests = log_requests + [math.log(i*1000)]
    requests = requests + [i*1000]

plt.plot(requests, times)
plt.show()
plt.plot(log_requests,times)
plt.show()


##############################################################################################################
"""
#Pour montrer la repartition de 1000 points sur la carte.
abs = [random.uniform(4.680, 4.830) for i in range(1000)]
ord = [random.uniform(45.730, 45.84) for i in range(1000)]
plt.scatter(abs, ord)


plt.show()
"""
