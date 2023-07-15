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

## Setup the pre-commit hook

To setup the pre-commit hook run the following command:

```bash
ln -s scripts/pre-commit.sh .git/hooks/pre-commit
```

Now everytime you commit the projects tests and linting and formatting checks will be run.
