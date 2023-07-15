[![Tests](https://github.com/MrRobot420/boilerplate-python-project/actions/workflows/unittest.yml/badge.svg?branch=main)](https://github.com/MrRobot420/boilerplate-python-project/actions/workflows/unittest.yml)

# Boilerplate Python Project

This is a boilerplate Python project that can be used to quickly get started with a new project.

## Contents

It includes:

-   `main.py` - A entrypoint for the projects code.
-   a `src` directory for the projects source code.
    -   a `config/settings.py` file for the projects settings which are loaded from a `.env` file.
    -   a `services` directory for the projects services.
    -   a `types` directory for the projects type definitions.
    -   a `utils` directory for the projects utility functions.
-   a `tests` directory for the projects tests.
-   a `requirements.txt` file for the projects dependencies.
-   linting and formatting configuration files for `pylint`, `mypy` and `black`.
-   a `.gitignore` file for ignoring standard python files and directories.
-   a `README.md` file for describing the project.
-   a `scripts/pre-commit.sh` script for running the projects tests and linting and formatting checks before committing.

It also includes a Dockerfile for building a Docker image that can be used to run the project.

## Installation

The first thing to do is to clone the repository:

```bash
$ git clone git@github.com:MrRobot420/openai-api.git
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```bash
(.venv) $ pip install -r requirements.txt
```

### Pre-Commit Hook

In order to install the pre-commit hook, run the following command:

```bash
pre-commit install
```

The will now run the script `pre-commit.sh` before every commit from now on.
You can find it in the `/scripts` folder.

It will run:

-   `unittests`
-   `pylint`
-   `mypy`

You can try it out by running:

```bash
pre-commit run --all-files
```

Enable the `-v` flag inside the .pre-commit-config.yaml file to see the verbose output of the script.
