import os
import subprocess
import argparse
from git import Repo
from .json_loader import load_json
from .github_requester import fetch_last_head_from_github


def concat_actions_to_single(actions_group) -> str:
    merged_command = ""
    for action_name, command in actions_group.items():
        merged_command += command + " && "

    merged_command += "echo 'Finished'"
    return merged_command


def main():
    """simply parses cli argument to get `abs_file_path` which is an absolute path to configs.json"""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help='Absolute path to `deployment-config.json`')
    # parse args and make a dict
    cli_arguments = vars(parser.parse_args())
    deployment_config_path = os.path.join(cli_arguments["file_path"])

    # display information about provided config-file.json
    print("Loading deployment configurations from %s...\n" % deployment_config_path)

    # `load_json` return dict of parsed actions
    parsed_actions = load_json(deployment_config_path)

    # extract every variable needed from parsed_actions
    repository_path = os.path.join(parsed_actions["configs"]["repository_path"])
    github_url = parsed_actions["configs"]["github_url"]
    github_access_token = parsed_actions["configs"]["access_token"]

    # init git repository
    repo = Repo.init(repository_path)

    # fetch last head `hash`
    last_head = repo.head.commit
    last_head = str(last_head)

    # fetch from github last remote branch sha (hash)
    print("Fetching from remote %s last head...\n" % github_url)
    remote_last_head = fetch_last_head_from_github(github_url, github_access_token)

    if remote_last_head != last_head:
        print("There were update in repository, running actions...\n")

        # change to repository directory to execute commands
        os.chdir(repository_path)

        all_actions = parsed_actions["actions"]

        for action_group_name, actions_group in all_actions.items():
            print("Action group `%s` in process" % action_group_name)

            all_actions = concat_actions_to_single(actions_group)

            subprocess.run(args=all_actions, shell=True)
    else:
        print("Remote last head {%s} is equal to local, nothing to do.")

