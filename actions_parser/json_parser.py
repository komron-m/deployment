import json
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
# end of def


def json_config_parser(json_data):
    """Parses yaml block, replaces placeholders (template: ${})"""

    # lookup dictionary for resolving placeholders
    new_block = {}

    for key, value in json_data["configs"].items():
        # grab key and value
        value = replace_placeholders(value, new_block)
        new_block[key] = value

    json_data["configs"] = new_block
# end of def


def json_actions_parser(json_data):
    # lookup dictionary for resolving placeholders
    dictionary = json_data["configs"]

    # iterate over actions_parser
    for action_name, action in json_data["actions"].items():

        # parse any placeholder found in `command` variable
        for desc, command in action.items():
            command = replace_placeholders(command, dictionary)
            action[desc] = command
# end of def


def load_json(file_path) -> dict:
    file = open(file_path, "r")
    json_data = json.load(file)

    json_config_parser(json_data)
    json_actions_parser(json_data)

    file.close()

    return json_data
