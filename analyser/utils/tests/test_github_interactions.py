from unittest.mock import MagicMock, call, patch

from analyser.utils.github_interactions import clone_repo, retrieve_repositories

FILE_PATH = "analyser.utils.github_interactions"


@patch(f"{FILE_PATH}.Path")
@patch(f"{FILE_PATH}.Repo")
def test_clone_repo(mock_repo: MagicMock, mock_path: MagicMock) -> None:
    # Arrange
    mock_path.exists.return_value = False
    # Act
    clone_repo("JackPlowman", "github-stats-prototype")
    # Assert
    mock_repo.clone_from.assert_called_once_with(
        "https://github.com/JackPlowman/github-stats-prototype.git",
        mock_path.return_value,
    )


@patch(f"{FILE_PATH}.Path")
@patch(f"{FILE_PATH}.Repo")
def test_clone_repo_exists(mock_repo: MagicMock, mock_path: MagicMock) -> None:
    # Arrange
    mock_path.exists.return_value = True
    # Act
    clone_repo("JackPlowman", "github-stats-prototype")
    # Assert
    mock_repo.clone_from.assert_not_called()


@patch(f"{FILE_PATH}.Github")
@patch(f"{FILE_PATH}.getenv")
def test_retrieve_repositories(mock_getenv: MagicMock, mock_github: MagicMock) -> None:
    # Arrange
    token = "TestToken"  # noqa: S105
    mock_getenv.side_effect = [token, "Test"]
    full_name = "Test3/Test4"
    mock_github.return_value.search_repositories.return_value = search_return = MagicMock(
        totalCount=1, list=[MagicMock(full_name=full_name)]
    )
    configuration = MagicMock(repository_owner="Test")
    # Act
    repositories = retrieve_repositories(configuration)
    # Assert
    mock_github.assert_called_once_with(token)
    mock_getenv.assert_has_calls([call("INPUT_GITHUB_TOKEN")])
    assert repositories == search_return
