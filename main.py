import os
import subprocess
from git import Repo
from github_requester import github_requester
from cli_args import cli_argument_parser
from actions_parser.json_parser import load_json
from actions_parser.json_querier import *


def main():
    cli_args = cli_argument_parser.get_cli_args()

    # load configuration and actions file
    actions_file_path = os.path.join(cli_args.getAbsFilePath())

    # `load_json` return dict of parsed actions
    parsed_actions = load_json(actions_file_path)

    # helper class, that queries dict for values
    actions_querier = JsonQuerier(parsed_actions)

    # init git repository
    repository_path = os.path.join(actions_querier.get_repository_path())
    repo = Repo.init(repository_path)

    # fetch last head `hash`
    last_head = repo.head.commit
    last_head = str(last_head)

    # fetch from github last remote branch sha (hash)
    remote_last_head = github_requester.fetch_last_head_from_github(
       actions_querier.get_github_url(),
       actions_querier.get_access_token()
    )

    if remote_last_head != last_head:
        # change to repository directory to execute commands
        os.chdir(repository_path)

        all_actions = actions_querier.get_all_actions()

        for action_name, action in all_actions.items():
            all_actions = concat_actions_to_single(action)

            subprocess.run(args=all_actions, shell=True)

            print("Action `%s` in process" % action_name)
