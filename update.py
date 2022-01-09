import requests
import json

repos = open("repos.json")
repoData = json.load(repos)

for repo in repoData["repos"]:
  print(repo)
  
