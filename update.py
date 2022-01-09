import requests
import json

repos = open("repos.json")
repoData = json.load(repos)
index = 0

for repo in repoData["repos"]:
  if (repo is not None and repo["owner"] is not None and repo["repoName"] is not None): 
    owner = repo["owner"]
    repoName = repo["repoName"]

    print(">----------<")
    print("Fetching latest versions: " + owner + "/" + repoName)
    try:
      res = requests.get("https://api.github.com/repos/" + owner + "/" + repoName + "/releases", headers={"Accept": "application/json"})
      responseData = json.loads(str("{\"data\": " + res.text + "}"))

      file = open("release-versions/" + repoName + "-latest.json", "w")
      file.write(json.dumps(responseData, indent=2, sort_keys=True))
      file.close()

      print("Latest version for: " + owner + "/" + repoName + " | " + responseData["data"][0]["tag_name"])
    except Exception as e: 
      print("Failed to update latest version for: " + owner + "/" + repoName)
      print("Reason:", end=" ")
      print(e)
  else:
    print("Failed to update latest version, for repo at index " + str(index) + " because insufficient data was supplied.")
  index += 1
