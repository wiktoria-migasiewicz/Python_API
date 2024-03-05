import requests
import datetime
import pprint
import json
import webbrowser

time_delta = datetime.timedelta(days=7)
search_date = int(datetime.datetime.timestamp(datetime.datetime.today() - time_delta))

params = {
    'site': 'stackoverflow',
    'sort': 'reputation',
    'order': 'desc',
    'fromdate': search_date,
    'tagged': 'python',
    'min': 160
}

r = requests.get('https://api.stackexchange.com/2.3/users/', params)
try:
    data = r.json()
except json.decoder.JSONDecodeError:
    print('Exception raised')
else:
    for user in data['items']:
        webbrowser.open(user['link'])



