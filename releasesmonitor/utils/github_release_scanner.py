import feedparser
import re

github_repo = 'https://github.com/coreos/prometheus-operator'

feed = feedparser.parse("{}/releases.atom".format(github_repo))

if feed and feed.entries:
    last_release = feed.entries[0]['id']
    release_version_match = re.search('v\d*\.\d*\.\d*$', last_release)

    if release_version_match:
        release_version = release_version_match.group(0)
        print("Repo {} - Last release version: {}".format(github_repo, release_version))
    else:
        print("Repo {} - Does not follow Semantic Versioning format".format(github_repo))
else:
    print("Repo {} - Does not have any release available".format(github_repo))
