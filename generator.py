from kafka import KafkaProducer
import time
import json
import random


generator_interval = 1
number_of_concurrent_requests = 109000
The kafka producer
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'), batch_size=0)

i = 0
while True:
    for _ in range(number_of_concurrent_requests):
        start = time.time()
        data = json.dumps({
            "data": {
                "latitude": random.uniform(45.730, 45.84), "longitude": random.uniform(4.680, 4.830), "timestamp": time.time()
            },
            "metadata": {
                "msisdn": str(random.randint(33600000000,33799999999)),
                "radius": 150
            }
        })
        producer.send('geoloc', data)
    end = time.time()
    time.sleep(generator_interval - end + start)
producer.close(0)



# Or using requests
# r = requests.post(URL, data)
# print(r.text)
