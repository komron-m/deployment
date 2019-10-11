class ConfigQuerier:
    """ ConfigQuerier is an API over config file (yaml or any), to make it more verbose to select
        values from `configs`,`jobs`, ...etc maps"""

    def __init__(self, parsed_actions):
        self.parsed_actions = parsed_actions

    def getRepositoryPath(self) -> str:
        return self.parsed_actions["configs"]["repository_path"]

    def getGitHubUrl(self) -> dict:
        return self.parsed_actions["configs"]["github_url"]

    def getJobs(self) -> dict:
        return self.parsed_actions["jobs"]

    def getWorkingBranch(self) -> str:
        return self.parsed_actions["configs"]["working_branch"]

    def getStdOutFilePath(self) -> str:
        return self.parsed_actions["configs"]["std_out"]

    def getStdErrFilePath(self) -> str:
        return self.parsed_actions["configs"]["std_err"]
