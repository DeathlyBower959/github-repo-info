import requests
import json

response = requests.get("https://api.github.com/repos/bozbez/win-capture-audio/releases")
print(json.dumps(json.loads(response.json()), index=4))
