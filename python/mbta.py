import json
import requests
import time
import datetime
import sys

if len(sys.argv) == 1:
	print("You must enter a station code!")
	exit()
else :
	url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=5VJxw0cEAEWShNPVo-iAtg&stop=' + sys.argv[1] + '&format=json'

response = requests.get(url)
data = json.loads(response.text)

stop_name = data["stop_name"]

print('Arrival information for: ' + stop_name) 

for mode in data['mode']:
	print('+- ' + mode['mode_name'])
	for route in mode["route"]:
		print('  +- ' + route['route_name'])
		for direction in route['direction']:
			print('    +- ' + direction['direction_name'])
			for trip in direction['trip']:
				print('      +- ' + time.strftime("%H:%M", time.localtime(int(trip['sch_arr_dt'])))
				+ ' (' + str(datetime.timedelta(seconds = int(trip['pre_away']))) + ')')
