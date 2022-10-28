from pprint import pprint

import requests

# url = 'https://api.exchangerate.host/latest'
# my_filter = {'rates': 'NZD'}
# response = requests.get(url, params=my_filter)
# data = response.json()
#
# print(data)

url = 'https://api.exchangerate.host/symbols'
response = requests.get(url)
data = response.json()

pprint(data)