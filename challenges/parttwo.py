#!/usr/bin/python3
import requests

# the URL you wish to post to
url = 'http://10.11.206.110:2224/login'

# the data you wish to post
joke = {'userans': 'slap'}

x = requests.post(url, data = joke)

print(x.text)

