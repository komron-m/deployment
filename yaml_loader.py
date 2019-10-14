import os
import yaml
import re


def replace_placeholders(some_string, dictionary):
    """if string has some placeholder then it's gonna be replaced with """

    if some_string is None:
        return ""

    # regex that detects a place-holder in some string
    regex_template = '(?:\${)(\w+)(?:})'

    # running regex against the string
    matches = re.findall(regex_template, some_string)

    # if found replace them
    if len(matches) > 0:

        # get unique values
        matches = set(matches)

        for match in matches:
            replace_template = "${%s}" % match
            some_string = some_string.replace(replace_template, dictionary[match])

    return some_string


def yaml_config_parser(yaml_file):
    """Parses yaml block, replaces placeholders (template: ${})"""

    # init new block for storing parsed values
    new_block = {}

    for line_from_block in yaml_file["configs"]:
        # grab key and value
        some_name = line_from_block["key"]
        value_to_be_parsed = line_from_block["value"]

        # store config key => value
        new_block[some_name] = replace_placeholders(value_to_be_parsed, new_block)

    yaml_file["configs"] = new_block


# end of def


def yaml_jobs_parser(yaml_file):
    """Parses yaml block, replaces placeholders (template: ${})
    mostly the same as yaml_config_parser function, but as a dictionary of placeholders it looks for
    configs map """

    new_block = {}
    configs = yaml_file["configs"]

    for line_from_block in yaml_file["jobs"]:
        # grab key and value
        some_name = line_from_block["name"]
        value_to_be_parsed = line_from_block["run"]

        # store config key => value
        new_block[some_name] = replace_placeholders(value_to_be_parsed, configs)

    yaml_file["jobs"] = new_block


def load_yaml(yaml_file_name="actions.yaml"):
    """Opens a yaml file and parses it, resolving placeholders bottom down order and return a dictionary"""

    # open actions stream (file)
    file_path = os.path.join(os.path.dirname(__file__), yaml_file_name)
    actions_yaml = open(file_path, "r")

    # load (parse) stream
    loaded_yaml_file = yaml.safe_load(actions_yaml)

    yaml_config_parser(loaded_yaml_file)
    yaml_jobs_parser(loaded_yaml_file)

    actions_yaml.close()

    return loaded_yaml_file
