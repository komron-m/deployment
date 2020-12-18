import os
from unittest import TestCase

from src.main import replace_placeholder_in_string, parse_keys, parse_actions, parse_config_file


class Test(TestCase):
    def test_replace_placeholder_in_string(self):
        test_data = [
            {
                "input": "John ${surname}",
                "placeholders": {
                    "surname": "Doe"
                },
                "expected": "John Doe",
            },
            {
                "input": "John ${surname} has ${amount} apples",
                "placeholders": {
                    "surname": "Doe",
                    "amount": "five"
                },
                "expected": "John Doe has five apples",
            },
            {
                "input": "John ${surname} has ${amount} apples and ${amount} oranges",
                "placeholders": {
                    "surname": "Doe",
                    "amount": "five"
                },
                "expected": "John Doe has five apples and five oranges",
            },
        ]

        for data in test_data:
            got = replace_placeholder_in_string(data["input"], data["placeholders"])
            self.assertEqual(data["expected"], got)

    def test_parse_keys(self):
        test_data = [
            {
                "json_data": {
                    "keys": {
                        "owner": "john_doe",
                        "remote": "origin",
                        "test": "/${owner}/${remote}/path"
                    }
                },
                "expected": {
                    "owner": "john_doe",
                    "remote": "origin",
                    "test": "/john_doe/origin/path"
                }
            }
        ]

        for data in test_data:
            got = parse_keys(data["json_data"])
            self.assertEqual(data["expected"], got)

    def test_parse_actions(self):
        test_data = [
            {
                "parsed_keys": {
                    "remote": "origin_name",
                    "working_branch": "master",
                    "some_folder": "/var/www/project/tmp",
                },
                "json_data": {
                    "actions": [
                        {
                            "description": "Will fetch changes from ${remote}",
                            "exe": "git pull ${remote} ${working_branch}"
                        },
                        {
                            "description": "Removes recursively ${some_folder} from machine",
                            "exe": "rm -rf ${some_folder}"
                        }
                    ]
                },
                "expected": [
                    {
                        "description": "Will fetch changes from origin_name",
                        "exe": "git pull origin_name master"
                    },
                    {
                        "description": "Removes recursively /var/www/project/tmp from machine",
                        "exe": "rm -rf /var/www/project/tmp"
                    }
                ]

            }
        ]

        for data in test_data:
            got = parse_actions(data["json_data"], data["parsed_keys"])
            self.assertEqual(data["expected"], got)

    def test_parse_config_file(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_config.json")
        keys, actions = parse_config_file(file_path)

        self.assertEqual({
            "repository_root": "/var/www/awesome-project",
            "remote": "origin",
            "ssh_key": "/opt/deployment/id_rsa",
            "working_branch": "master"
        }, keys)

        self.assertEqual([
            {
                "description": "Install new dependencies",
                "exe": "composer install --ignore-platform-reqs --no-interaction"
            },
            {
                "description": "Clean cache values",
                "exe": "php /var/www/awesome-project/artisan cache:clear"
            },
            {
                "description": "Run migrations for master",
                "exe": "php /var/www/awesome-project/artisan migrate"
            }
        ], actions)
