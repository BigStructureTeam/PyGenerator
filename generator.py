from kafka import KafkaProducer
import time
import json
import random
import ujson

#The kafka producer
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'], batch_size=0, acks=0) # value_serializer=lambda v: v.encode('utf-8')

rands = [[random.uniform(45.79, 45.84),random.uniform(4.79, 4.95),str(33600000000 + random.randint(0,199999999))] for i in range(1000)]

count = 0
while True:
    for _ in range(1000):
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
        producer.send('geodata-6', data)
    count = count + 1000000
    print count
    # print("time used:")
    # print(end - start)
    # if generator_interval - end + start > 0:
    	# time.sleep(generator_interval - end + start)


producer.close(0)



# Or using requests
# r = requests.post(URL, data)
# print(r.text)
