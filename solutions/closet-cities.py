import requests
from math import *
import json

# 4 million .... https://github.com/lutangar/cities.json/blob/master/cities.json?raw=true

home = (46.542816, 6.637191)

def get_github_file(url):
	headers = { 'Content-Type': 'application/json' }
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode(response.encoding))
	else:
		print("*** ERROR! Response ",response.status_code," ***")
		return None

def get_distance( location1, location2):
    # Use haversine formula
    radius = 6273
    lat1 = location1[0] * pi/180
    lat2 = location2[0] * pi/180
    lon1 = location1[1] * pi/180
    lon2 = location2[1] * pi/180
    dlat = abs(lat2 - lat1)
    dlon = abs(lon2 - lon1)
    a = (sin(dlat/2)**2) + cos(lat1) * cos(lat2) * (sin(dlon/2) ** 2)
    c = 2 * atan2( sqrt(a), sqrt(1-a) )
    d = radius * c
    return d

if __name__ == "__main__":
	# Load data
	print("Downloading data (this might take a while...)")
	cities = get_github_file("https://github.com/lutangar/cities.json/blob/master/cities.json?raw=true")
	print("Calculating...")

	# Calculate distance for all cities
	for city in cities:
		distance = get_distance(home, (float(city['lat']), float(city['lng'])))
		city['distance'] = round(distance)

	# Sort by distance
	cities = sorted(cities, key=lambda k: k['distance']) 
	import urllib.parse as p

	# Print results
	for city in cities:
		print("{}: {}".format(p.unquote(city['name']).ljust(30), city['distance']))
