import json
import logging
import os
import re
import subprocess
import sys


def replace_placeholder_in_string(str_value: str, keys: dict) -> str:
    """find in string ${placeholder} pattern and replaces it with item from keys dictionary"""
    regex_template = '(?:\${)(\w+)(?:})'
    matches = re.findall(regex_template, str_value)
    if len(matches) > 0:
        matches = set(matches)
        for match in matches:
            replace_template = "${%s}" % match
            str_value = str_value.replace(replace_template, keys[match])
    return str_value


def parse_keys(json_data) -> dict:
    """traverse over keys (dictionary) and create new dictionary with replaced placeholders"""
    parsed_keys = {}
    keys = json_data["keys"]
    for key, value in keys.items():
        parsed_keys[key] = replace_placeholder_in_string(value, keys)
    return parsed_keys


def parse_actions(json_data, keys: dict) -> list:
    """traverse over actions, replace placeholders in description and actions"""
    li = []
    for i in range(len(json_data["actions"])):
        description = replace_placeholder_in_string(json_data["actions"][i]["description"], keys)
        exe = replace_placeholder_in_string(json_data["actions"][i]["exe"], keys)
        li.append({
            "description": description,
            "exe": exe
        })
    return li


def parse_config_file(file_path: str) -> (dict, list):
    """open json file and parse keys and actions"""
    file = open(file_path, "r")
    json_data = json.load(file)
    file.close()

    parsed_keys = parse_keys(json_data)
    actions = parse_actions(json_data, parsed_keys)
    return parsed_keys, actions


def run_actions(file_path: str):
    # set logger prefix
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p :::')

    # display information about provided config-file.json
    logging.warning("loading configurations file from `test_conf.json`")
    keys, actions = parse_config_file(file_path)

    # cd into git repo
    logging.warning("cd into project dir `%s`" % keys["repository_root"])
    os.chdir(keys["repository_root"])

    # get last head hash
    last_head = subprocess.run(args="git rev-parse HEAD", shell=True, capture_output=True)
    if last_head.returncode != 0:
        return
    last_head = last_head.stdout.decode("UTF-8")

    # clean working directory and checkout to working branch
    logging.warning("clean working directory and checkout to working branch")
    checkout_cmd = "git checkout . && git clean -fd && git checkout ${working_branch}"
    checkout_cmd = replace_placeholder_in_string(checkout_cmd, keys)
    cleaning_cmd = subprocess.run(args=checkout_cmd, shell=True)
    if cleaning_cmd.returncode != 0:
        return

    # add ssh-key to session
    logging.warning("add ssh-key to session and pull from origin")
    add_ssh_cmd = "ssh-add ${ssh_key} && git pull ${remote} ${working_branch}"
    add_ssh_cmd = replace_placeholder_in_string(add_ssh_cmd, keys)
    add_ssh_cmd = subprocess.run(args=add_ssh_cmd, shell=True)
    if add_ssh_cmd.returncode != 0:
        print("")
        # return

    # get last head hash
    head_after_pull = subprocess.run(args="git rev-parse HEAD", shell=True, capture_output=True)
    head_after_pull = head_after_pull.stdout.decode("UTF-8")
    if head_after_pull == last_head:
        logging.warning("no updates were loaded from origin, exiting")
        # return

    # handle user actions
    info_template = "*\t{} ===> `{}`\n"
    info = "following commands were parsed and will run in one row:\n"
    command_template = "%s"
    commands = ""
    for action in actions:
        info += info_template.format(action["description"], action["exe"])
        commands += command_template % action["exe"]
        commands += " && "
    commands = commands[:-4]

    logging.warning(info)
    subprocess.run(args=commands, shell=True)


if __name__ == '__main__':
    args = sys.argv
    run_actions(args[1])
