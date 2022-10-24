import os, json

from django.conf import settings

@app.task(name="get-github-repos")
def get_github_repos(keyword):
    """Get github repos"""
    url = "https://api.github.com/search/repositories?q={}".format(keyword)
    response = requests.get(url)
    return response.json()
