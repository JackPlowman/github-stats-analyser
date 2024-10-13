from os import getenv
from sys import exit

REQUIRED_ENVIRONMENT_VARIABLES = ["INPUT_GITHUB_TOKEN", "INPUT_REPOSITORY_OWNER"]


"""Check that the required environment variables are set."""
for variable in REQUIRED_ENVIRONMENT_VARIABLES:
    if getenv(variable) is None:
        if "INPUT_" in variable:
            print(f'Error: Required environment variable {variable.removeprefix("INPUT_")} is not set')
        else:
            print(f"Error: Required environment variable {variable} is not set")
        exit(1)
