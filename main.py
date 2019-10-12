import os
import subprocess
from git import Repo
import github_fetcher
import yaml_loader
import config_querier
import logger

# load and pars yaml configurations
actions = yaml_loader.load_yaml()

# queries config file
configQuerier = config_querier.ConfigQuerier(actions)

# init git repository
repo = Repo.init(os.path.join(configQuerier.getRepositoryPath()))

# fetch last head `hash`
last_head = repo.head.commit

# fetch from github
remote_last_head = github_fetcher.fetch_last_head_from_github(
    configQuerier.getGitHubUrl(),
    configQuerier.getAccessToken()
)

# init simple file logger instance
log = logger.Logger(
    os.path.join(configQuerier.getStdOutFilePath()),
    os.path.join(configQuerier.getStdErrFilePath())
)

if remote_last_head != last_head:
    # change to repository directory to execute commands
    os.chdir(configQuerier.getRepositoryPath())

    # iterating over key (job_desc) and value (job_command)
    # redirecting stdout and stderr to files
    for job_desc, job_command in configQuerier.getJobs().items():
        print("job: `%s`" % job_desc)
        subprocess.run(
            args=job_command,
            stdout=log.getStdOutFile(),
            stderr=log.getStdErrFile(),
            shell=True
        )

log.closeFiles()
