"""
Proof of concept self-documentation of current revision, and deploy
notification to Rollbar.
"""

import os, git, urllib, requests

with open("/home/kris/rollbar_key") as rollbar_key_file:
    ROLLBAR_KEY = rollbar_key_file.read().strip()

DEBUG = True

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
commmitMessage = commit.message

# Notify rollbar of new deploy for deploy tracking
requestData = {
    "access_token": ROLLBAR_KEY,
    "environment": "development" if DEBUG else "production",
    "revision": commitID,
    "comment": commitMessage,
}
request = requests.post("https://api.rollbar.com/api/1/deploy/", requestData)
