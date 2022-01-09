import requests
import json

repos = open("repos.json")
repoData = json.load(repos)

index = 0

for repo in repoData["repos"]:
  if (repo is not None and repo["owner"] is not None and repo["repoName"] is not None): 
    print(">----------<")
    print("Fetching latest versions: " + repo["owner"] + "/" + repo["repoName"])
    try:
      response = requests.get("https://api.github.com/repos/" + repo["owner"] + "/" + repo["repoName"] + "/releases")
      file = open("release-versions/" + repo["repoName"] + ".txt", "w")
      file.write(json.dumps(json.loads(response.json()), indent=4, sort_keys=True))
      file.close()
      print("Latest version for: " + repo["owner"] + "/" + repo["repoName"] + " | " + response.json()["tag_name"])
    except Exception as e: 
      print("Failed to update latest version for: " + repo["owner"] + "/" + repo["repoName"])
      print("Reason: ")
      print(e)
  else:
    print("Failed to update latest version, for repo at index " + str(index) + " because insufficient data was supplied.")
  index += 1
