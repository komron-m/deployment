import argparse


def parse_cli_args():
    """simply parses cli arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("abs_file_path", type=str, help='Absolute path to `actions.json`')

    return vars(parser.parse_args())


class CliArgs:
    """simple querier for dictionary of arguments"""
    def __init__(self, args):
        self.args = args

    def getAbsFilePath(self) -> str:
        return self.args["abs_file_path"]


def get_cli_args() -> CliArgs:
    """inits a below Class for parsing"""
    return CliArgs(parse_cli_args())
