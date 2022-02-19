# GitHub Repo Information

This is just a simple repository used to get simple information about repositories

# Latest Releases
If you want a specific repo, create an issue with this format
```
Repo Owner: OwnerName or OrgName
Repo Name: Name

Only put this if you need it to check more frequently than it currently is
cron: * * * * *
```

---
### Notes:
 - Runs every 30 minutes (`*/30 * * * *`)
 - Even after it finds the new version of the app, it takes 5 minutes to update because of GitHub caching
---

### JSON Format
The releases are located in an array, under the key "data", as you can see in the representation below.

```json
{
  "data": [
    {
      "assets": [
        {
          "browser_download_url": "",
          "content_type": "",
          "created_at": "",
          "download_count": 0,
          "id": 0,
          "label": "",
          "name": "",
          "node_id": "",
          "size": 0,
          "state": "",
          "updated_at": "",
          "uploader": {
            "avatar_url": "",
            "events_url": "",
            "followers_url": "",
            "following_url": "",
            "gists_url": "",
            "gravatar_id": "",
            "html_url": "",
            "id": 0,
            "login": "",
            "node_id": "",
            "organizations_url": "",
            "received_events_url": "",
            "repos_url": "",
            "site_admin": false,
            "starred_url": "",
            "subscriptions_url": "",
            "type": "",
            "url": ""
          },
          "url": ""
        }
      ],
      "assets_url": "",
      "author": {
        "avatar_url": "",
        "events_url": "",
        "followers_url": "",
        "following_url": "",
        "gists_url": "",
        "gravatar_id": "",
        "html_url": "",
        "id": 0,
        "login": "",
        "node_id": "",
        "organizations_url": "",
        "received_events_url": "",
        "repos_url": "",
        "site_admin": false,
        "starred_url": "",
        "subscriptions_url": "",
        "type": "",
        "url": ""
      },
      "body": "",
      "draft": false,
      "html_url": "",
      "id": 0,
      "name": "",
      "node_id": "",
      "prerelease": false,
      "published_at": "",
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": ""
      },
      "tag_name": "",
      "tarball_url": "",
      "target_commitish": "",
      "upload_url": "",
      "url": "",
      "zipball_url": ""
    }
  ]
}
```
