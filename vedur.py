import requests
import xml.etree.ElementTree as ET
import codecs
from datetime import date

d = date.today()
year = str(d.year)

r = requests.get('https://xmlweather.vedur.is/?op_w=xml&type=obs&lang=is&view=xml&ids=1;422&params=T;D;W;F')
text = r.text
text = text[:-5] #Formating the string to please ElementTree

with codecs.open('weather.xml', 'w', 'utf-8-sig') as f:
	f.write(text)

tree = ET.parse('weather.xml')
root = tree.getroot()

stations = []

for station in root.findall('station'):
	name = station.find('name').text
	time = station.find('time').text
	temp = station.find('T').text
	wind_dir = station.find('D').text
	wind = station.find('F').text
	description = station.find('W').text
	
	if description == None: #If there is no description of the weather
		description = "engin"

	print(f'{name}	| {d.day}-{d.month} \'{year[-2:]} {time[:-3]} | veðurlýsing: {description}	| hiti {temp}°	| vindur {wind_dir} {wind} m/s')