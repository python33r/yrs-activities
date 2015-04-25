import requests
from PIL import Image, ImageDraw

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"

response = requests.get(url)

if response.status_code == 200:

    image = Image.open("map-base.png")
    canvas = ImageDraw.Draw(image)

    data = response.json()
    for quake in data["features"]:
        coords = quake["geometry"]["coordinates"]
        x = 3*int(float(coords[0]) + 180)
        y = 3*int(90 - float(coords[1]))
        canvas.rectangle((x-2, y-2, x+2, y+2), fill="#f00")

    image.save("map.png")

else:
    print("Error: status code", response.status_code)
