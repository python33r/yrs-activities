import requests
from maps import google_map

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    map_data = []
    for quake in data["features"]:
        coords = quake["geometry"]["coordinates"]
        info = quake["properties"]["title"]
        map_data.append((coords[0], coords[1], info))

    google_map(map_data, "map.html")

else:
    print("Error: status code", response.status_code)
