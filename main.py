import os
import subprocess
from git import Repo
from github import github_fetcher
from yaml_parser import yaml_loader
from helpers import config_querier
from logger import logger


def main():
    # load and pars yaml configurations
    action_yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "actions.yaml")
    actions = yaml_loader.load_yaml(action_yaml_path)

    # queries config file
    config_query = config_querier.ConfigQuerier(actions)

    # init git repository
    repo = Repo.init(os.path.join(config_query.getRepositoryPath()))

    # fetch last head `hash`
    last_head = repo.head.commit
    last_head = str(last_head)

    # fetch from github
    remote_last_head = github_fetcher.fetch_last_head_from_github(
        config_query.getGitHubUrl(),
        config_query.getAccessToken()
    )

    # init simple file logger instance
    log = logger.Logger(
        os.path.join(config_query.getStdOutFilePath()),
        os.path.join(config_query.getStdErrFilePath())
    )

    if remote_last_head != last_head:
        # change to repository directory to execute commands
        os.chdir(config_query.getRepositoryPath())

        # iterating over key (job_desc) and value (job_command)
        # redirecting stdout and stderr to files
        for job_desc, job_command in config_query.getJobs().items():
            print("job: `%s`" % job_desc)
            subprocess.run(
                args=job_command,
                stdout=log.getStdOutFile(),
                stderr=log.getStdErrFile(),
                shell=True
            )

    log.closeFiles()
