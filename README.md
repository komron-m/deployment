Automate adding `manually ssh-key, cleaning directory from untracked files, pulling from remote` etc... After pulling
easily configure `post steps`. This package can be added into your CI/CD pipeline. Tested on python >= 3.7

### Getting started

```bash
# simply clone repo and cd into cloned repo
git clone git@github.com:komron-m/deployment.git && cd deployment
# after cloning copy test_config.json and set all actions and `keys`
cp tests/test_config.json /path/to/project_conf.json
# run script with one argument
python src/main.py /path/to/project_conf.json

# or use it as package after installing 
pip install githubdeployment
```

### Configs

```json
{
  "keys": {
    "remote": "origin",
    "repository_root": "/var/www/awesome-project",
    "ssh_key": "/opt/deployment/id_rsa",
    "working_branch": "master"
  },
  "actions": [
    {
      "description": "Install new dependencies",
      "exe": "composer install --ignore-platform-reqs --no-interaction"
    }
  ]
}
```

- `keys` are mandatory, make sure all permissions are set for files and directories.
- `actions` contain a list of action, where `description` is plain message for logging and `exe` is command that run
  right after `git pull ${remote} ${working_branch}`. All actions run as one `pipe`.
