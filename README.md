## Simple auto-deployment tool based on GitHub API
Requires python >= 3.6

### Getting started
```shell script
# pip install github_deployment
```

#### Then create your own `deployment.json` based on provided `deployment.example.json`.
```python
# create deployment.py and following lines
from deployment.main import deploy
deploy('/path/to/deployment.json')
```

#### Run
```shell script
# python deployment.py
```

### deployment.json `config` block explained
  - `working_branch` - *Which branch you want to pull from*
  - `access_token` - *Your access token if repository is private (if repo is not private just leave it blank )* [github access tokens](https://developer.github.com/v3/auth/)
  - `path_to_ssh_key` - *Where your deployment key is placed*, [github deployment keys](https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys) 
  - `repository_path` - *Path to root folder of your project*
  - `github_url` - *Github api which will be queried when main.py is activated* [github api](https://developer.github.com/v3/git/commits/)

All config keys are mandatory, make sure all permissions are set for files and directories.
