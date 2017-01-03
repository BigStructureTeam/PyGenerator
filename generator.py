import requests
import grequests
#import requests
import json

number_of_requests_package = 100
number_of_concurrent_requests = 100
local = True

# The URL where to post data
production_url = 'https://yagan.herokuapp.com/newGeo'
local_url = 'http://127.0.0.1:3000/newGeo'
URL = local_url if local else production_url

# Data to send (here in data.json file)
with open("./data.json") as json_data:
    data = json.load(json_data)

i = 0
r = []
while i < number_of_requests_package:
    # Easy asynchronous HTTP Requests
    r = (grequests.post(URL, data = data) for i in range(0, number_of_concurrent_requests))
    response = grequests.map(r)
    i += 1

# Or using requests
# r = requests.post(URL, data)
# print(r.text)