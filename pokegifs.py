import json
import requests
import os

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"]) # should be "pikachu"
print(body["types"])
print(body["id"])

key = os.environ.get("GIPHY_KEY")
url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
requests.get(url)