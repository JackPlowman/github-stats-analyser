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


def test_configuration__generate_action_summary_table() -> None:
    # Arrange
    environ["INPUT_REPOSITORY_OWNER"] = repo_owner = "test2"
    environ["INPUT_GITHUB_TOKEN"] = "TestToken"  # noqa: S105
    configuration = Configuration()
    # Act
    action_summary_table = configuration.generate_action_summary_table()
    # Assert
    assert action_summary_table == f"| Key | Repository Owner |\n| --- | ---------------- |\n| Value | {repo_owner} |"
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]
    del environ["INPUT_GITHUB_TOKEN"]
