from os import environ

from analyser.utils.configuration import Configuration


def test_configuration() -> None:
    # Arrange
    environ["INPUT_REPOSITORY_OWNER"] = repo_owner = "test2"
    environ["INPUT_GITHUB_TOKEN"] = fake_token = "TestToken"  # noqa: S105
    configuration = Configuration()
    # Assert
    assert configuration.repository_owner == repo_owner
    assert configuration.github_token == fake_token
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]
    del environ["INPUT_GITHUB_TOKEN"]
