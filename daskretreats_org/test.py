"""
Proof of concept self-documentation of current revision, and deploy
notification to Rollbar.
"""

import os, git, urllib, pycurl

# Path handling
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

# Git revision/branch checking
repo = git.Repo.init(PROJECT_ROOT)
commit = repo.commit()
nameRev = str(commit.name_rev)
nameRevList = nameRev.split()
commitID = nameRevList[0]
branchName = nameRevList[1]

# Curl deploy notice
curl = pycurl.Curl()
curl.setopt(curl.URL, "https://api.rollbar.com/api/1/deploy/")
postData = {
    "access_token": ROLLBAR_KEY,
    "environment": 'development' if DEBUG else 'production',
    "revision": commitID,
}
postFields = urllib.urlencode(postData)
curl.setopt(curl.POSTFIELDS, postFields)
curl.perform()
curl.close()
