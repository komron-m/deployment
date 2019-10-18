def concat_actions_to_single(action) -> str:
    single_command = ""

    for action_name, command in action.items():
        single_command += command + " && "

    single_command += "echo 'Success'"

    return single_command


class JsonQuerier:
    """ ConfigQuerier is an API over config file (yaml or any), to make it more verbose to select
        values from `configs`,`jobs`, ...etc maps"""

    def __init__(self, actions_data):
        self.actions_data = actions_data

    def get_repository_path(self) -> str:
        return self.actions_data["configs"]["repository_path"]

    def get_github_url(self) -> str:
        return self.actions_data["configs"]["github_url"]

    def get_access_token(self) -> str:
        return self.actions_data["configs"]["access_token"]

    def get_all_actions(self) -> dict:
        return self.actions_data["actions"]
