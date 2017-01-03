import requests
import grequests
#import requests
import json

number_of_requests = 1

# The URL where to post data
# URL = 'https://yagan.herokuapp.com/newGeo'
URL = 'http://127.0.0.1:3000/newGeo'

# Data to send (here in data.json file)
with open("./data.json") as json_data:
    data = json.load(json_data)

# Easy asynchronous HTTP Requests
r = (grequests.post(u, data = data) for u in [URL])

friends = grequests.map(r)
print(friends[0].text)

# Or using requests
# r = requests.post(URL, data)
# print(r.text)