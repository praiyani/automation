import json
import datetime
import requests
import geocoder
from pprint import pprint
#import socket
#import ipgetter

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

def getIpAddress():
	return requests.get('http://ip.42.pl/raw').text

def getlocationbyip(ipaddress):
	g = geocoder.freegeoip(ipaddress)
	return g

def getWeatherByLatLong(lat, long):
	key = 'f24f8822a5cf638bd40bf6f2588c2d93'
	url = 'http://api.openweathermap.org/data/2.5/weather?lat={' + str(lat) + '}&lon={' + str(long) + '}&appid=' + key
	print url
	resp = requests.get(url)
	return resp.json()
	
def runner():
	print 'Getting Weather information. Please wait!!!'
	ipaddress = getIpAddress()
	geolocation = getlocationbyip(ipaddress)
	
	lat = geolocation.json['lat'] 
	lng = geolocation.json['lng']
	
	print json.dumps(getWeatherByLatLong(lat, lng))
	
if __name__ == "__main__": 
	runner()
