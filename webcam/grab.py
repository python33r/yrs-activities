import requests

url = "http://millenniumsquare.a-q.co.uk/images/image.jpg"

response = requests.get(url)

if response.status_code == 200:
    with open("webcam.jpg", "wb") as outfile:
        outfile.write(response.content)
else:
    print("Error: cannot access image")
