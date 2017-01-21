from kafka import KafkaProducer
import time
import json
import random


generator_interval = 1
number_of_concurrent_requests = 2500
#The kafka producer
producer = KafkaProducer(bootstrap_servers = ['172.31.253.60:9092'], batch_size=0, acks=0) # value_serializer=lambda v: v.encode('utf-8')
count  = 0
# i = 0
while True:

    # for i in range(number_of_concurrent_requests):

	# if (i==0):
		# start = time.time()

    data = json.dumps({
        "data": {
            "latitude": random.uniform(45.730, 45.84), "longitude": random.uniform(4.680, 4.830), "timestamp": time.time()
        },
        "metadata": {
            "msisdn": str(random.randint(33600000000,33799999999)),
            "radius": 150
        }
    }).encode('utf-8')


    producer.send('geodata-6', data)
    count = count + 1 
    # end = time.time()

    if count % 10000 == 0:
    	print count
    # print("time used:")
    # print(end - start)
    # if generator_interval - end + start > 0:
    	# time.sleep(generator_interval - end + start)


producer.close(0)



# Or using requests
# r = requests.post(URL, data)
# print(r.text)
