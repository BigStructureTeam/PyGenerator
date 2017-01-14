import time
import json
import random
import math
import matplotlib.pyplot as plt

#Pour determiner le maximum de requetes en 1s:

number_of_concurrent_requests = 109000
start = time.time()
for _ in range(number_of_concurrent_requests):
    data = json.dumps({
        "data": {
            "latitude": random.uniform(45.730, 45.84), "longitude": random.uniform(4.680, 4.830), "timestamp": time.time()
        },
        "metadata": {
            "msisdn": str(random.randint(33600000000,33799999999)),
            "radius": 150
        }
    })
end = time.time()
print "La production de " + str(number_of_concurrent_requests) + " requetes a pris " + str(end - start) + " secondes"

############################################################################################################

#Pour tracer les performances en fonction du temps:
log_requests=[]
requests=[]
times=[]

for i in [1,3,10,30,100,300,1000,3000,10000,30000,100000,300000,1000000,3000000]:
    start = time.time()
    for _ in range(i):
        data = json.dumps({
            "data": {
                "latitude": random.uniform(45.730, 45.84), "longitude": random.uniform(4.680, 4.830), "timestamp": time.time()
            },
            "metadata": {
                "msisdn": str(random.randint(33600000000,33799999999)),
                "radius": 150
            }
        })
    end = time.time()
    times = times + [end-start]
    log_requests = log_requests + [math.log(i)]
    requests = requests + [i]

plt.plot(requests, times)
plt.show()

plt.plot(log_requests,times)
plt.show()


##############################################################################################################

#Pour montrer la repartition de 1000 points sur la carte.
abs = [random.uniform(4.680, 4.830) for i in range(1000)]
ord = [random.uniform(45.730, 45.84) for i in range(1000)]
plt.scatter(abs, ord)


plt.show()
