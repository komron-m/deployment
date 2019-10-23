import requests


def fetch_last_head_from_github(github_url, token) -> str:
    """fetches last head hash from github
    maybe there is a better ways to check whether a branch head was updated
    """

    headers = {
        "Accept": "application/vnd.github.VERSION.sha",
        "Authorization": "token %s" % token
    }
    resp = requests.get(github_url, headers=headers)

    return resp.content.decode("utf-8")
