# Changelog
All notable changes to this project will be documented in this file.

## [2.0.0] - 2020-12-18
Changes:
    - Simplified project. From this point no github access tokens are required.
    Also, outside from the box this package will pull from origin last changes (with .git) and then
    start executing actions of user.

## [1.0.0] - 2019-10-23
Changes:
    - Completely reworked project structure, added LICENCE, packaging tools.
    Moved from .yaml based configuration to .json format.         

## [0.0.1] - 2019-10-15
Changes:
    - Now actions.yaml is not searched by default in project repository,
    instead, you need to manually pass a `global` path to a file via
    command line
