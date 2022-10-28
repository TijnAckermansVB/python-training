from pprint import pprint
import requests


url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
#my_filter = {"kenteken": "HL747R"}
my_filter = {'merk': 'TESLA', 'eerste_kleur': 'ROOD'}
r = requests.get(url, params=my_filter).json()
[print(x['kenteken']) for x in r]
#pprint(len(r))