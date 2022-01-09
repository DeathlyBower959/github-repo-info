import requests
import json

repos = open("repos.json")
repoData = json.load(repos)

for repo in repoData["repos"]:
  response = requests.get("https://api.github.com/repos/" + repo.owner + "/" + repo.repoName + "/releases")

  file = open("release-versions/" + repo.repoName + ".txt", "w")
  f.write(response.json())
  f.close()
