import os
import requests
import requests.exceptions
import json

repos = open("repos.json")
repoData = json.load(repos)

alreadyRetrieved = []


def isRetrieved(owner, repoName):
    return {owner, repoName} in alreadyRetrieved


for index, repo in enumerate(repoData['repos']):
    print(">----------<")

    if (repo is None or repo["owner"] is None or repo["repoName"] is None):
        print(
            f"Failed to update latest version, for repo at index {str(index)} because insufficient data was supplied.")
        continue

    owner = repo["owner"]
    repoName = repo["repoName"]

    if (isRetrieved(owner, repoName)):
        print(
            f'Skipped fetching versions for {owner}/{repoName} as it was already fetched.')
        continue

    print(f"Fetching latest versions: {owner}/{repoName}")
    try:
        res = requests.get("https://api.github.com/repos/" + owner + "/" +
                           repoName + "/releases", headers={"Accept": "application/json"})
        res.raise_for_status()
        
        responseData = json.loads(str("{\"data\": " + res.text + "}"))
        latestVersion = responseData["data"][0]["tag_name"]

        if not os.path.exists(f"./release-versions/{owner}"):
            os.makedirs(f'./release-versions/{owner}')

        file = open(
            f"release-versions/{owner}/{repoName}.json", "w")
        file.write(json.dumps(responseData, indent=2, sort_keys=True))
        file.close()

        alreadyRetrieved.append({
            owner,
            repoName
        })

        print(f"Latest version for: {owner}/{repoName} | {latestVersion}")
    except requests.exceptions.HTTPError:
        print(f'Failed to find repo {owner}/{repoName}')
    except Exception as e:
        print(f"Failed to update latest version for: {owner}/{repoName}")
        print("Reason:", end=" ")
        print(e)

print(">----------<")

print('Cleaning Up...')


def noLongerRequired(owner, repoName):
    if ({'owner': owner, 'repoName': repoName} not in repoData['repos']):
        os.remove(f"./release-versions/{owner}/{repoName}.json")
        print(f'{owner}/{repoName} removed!')


for owner in os.listdir('release-versions'):
    for repo in os.listdir(f'release-versions/{owner}'):
        noLongerRequired(owner, os.path.splitext(repo)[0])

    if (len(os.listdir(f'./release-versions/{owner}')) == 0):
        os.rmdir(f'./release-versions/{owner}')
        print(f'Removed {owner}!')
