### Simple auto-deployment tool based on GitHub API
Requires python >= 3.6

### Getting started
First install dependencies:

```shell script
# pip install gitpython
# pip install pyyaml
# pip install requests 
```

Then create your own `actions.yaml` based on provided `actions.yaml.example` and run:

```python
# python main.py
```

### actions.yaml `config` block explained
  - `working_branch` - *Which branch you want to pull from*
  - `access_token` - *Your access token if repository is private (if repo is not private just leave it blank )* [github access tokens](https://developer.github.com/v3/auth/)
  - `path_to_ssh_key` - *Where your deployment key is placed*, [github deployment keys](https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys) 
  - `repository_path` - *Path to root folder of your project*
  - `github_url` - *Github api which will be queried when main.py is activated* [github api](https://developer.github.com/v3/git/commits/)
  - `std_out` - *Where jobs outputs will be stored*
  - `std_err` - *Where jobs errors will be stored*

All config keys are mandatory, make sure all permissions are set for files and directories.
