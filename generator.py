import requests
import grequests
#import requests
import json

number_of_requests = 1

# The URL where to post data
URL = 'http://yaga.herokuapp.com'

# Data to send (here in data.json file)
with open("./data.json") as json_data:
    data = json.load(json_data)

# Easy asynchronous HTTP Requests
r = (grequests.post(u, data = data) for u in [URL])

friends = grequests.map(r)
print(friends[0].json)

# Or using requests
# r = requests.post(github_url, data)