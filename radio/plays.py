import requests

url = "http://www.bbc.co.uk/programmes/music/artists/charts.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for artist in data["artists_chart"]["artists"]:
        if artist["plays"] > 40:
            print(artist["plays"], artist["name"])
else:
    print("Error: status code", response.status_code)
