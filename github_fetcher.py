import requests
import re


def fetch_last_head_from_github(github_url):
    """fetches last head hash from github
    maybe there is a better ways to check whether a branch head was updated ??
    TODO: find best approach
    """
    resp = requests.get(github_url)
    resp_data = resp.json()
    resp_url = resp_data["url"]

    remote_last_head = re.findall('(?:commits.)(\w{40})$', resp_url)

    return remote_last_head[0]
