import requests

response = requests.get("https://api.github.com/repos/bozbez/win-capture-audio/releases")
print(response.json())
