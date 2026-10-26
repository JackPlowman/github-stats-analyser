from typing import TYPE_CHECKING

from analyser.utils.configuration import Configuration

if TYPE_CHECKING:
    import pytest


def test_configuration(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    repo_owner = "test2"
    monkeypatch.setenv("INPUT_REPOSITORY_OWNER", repo_owner)
    fake_token = "TestToken"  # noqa: S105
    monkeypatch.setenv("INPUT_GITHUB_TOKEN", fake_token)
    configuration = Configuration()
    # Assert
    assert configuration.repository_owner == repo_owner
    assert configuration.github_token == fake_token
