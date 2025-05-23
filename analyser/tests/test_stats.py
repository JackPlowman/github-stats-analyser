from unittest.mock import MagicMock, patch

from analyser.stats import (
    create_repository_statistics,
    generate_output_file,
    generate_statistics,
)

FILE_PATH = "analyser.stats"


@patch(f"{FILE_PATH}.retrieve_repositories")
@patch(f"{FILE_PATH}.clone_repo")
@patch(f"{FILE_PATH}.remove_excluded_files")
@patch(f"{FILE_PATH}.create_repository_statistics")
@patch(f"{FILE_PATH}.DataFrame")
def test_generate_statistics(
    mock_data_frame: MagicMock,
    mock_create_repository_statistics: MagicMock,
    _mock_remove_excluded_files: MagicMock,
    mock_clone_repo: MagicMock,
    mock_retrieve_repositories: MagicMock,
) -> None:
    # Arrange
    repository = MagicMock()
    repository.owner.login = owner = "JackPlowman"
    repository.name = repo_name = "github-stats-prototype"
    mock_retrieve_repositories.return_value = [repository]
    mock_clone_repo.return_value = "TestPath"
    mock_create_repository_statistics.return_value = catalogued_repository = MagicMock(
        repository_name="Test1", total_files=10, commits=[], total_commits=0
    )
    configuration = MagicMock(repository_owner="test")
    # Act
    output = generate_statistics(configuration)
    # Assert
    assert output == mock_data_frame.return_value
    mock_retrieve_repositories.assert_called_once_with(configuration)
    mock_clone_repo.assert_called_once_with(owner, repo_name)
    mock_create_repository_statistics.assert_called_once_with(repo_name, "TestPath")
    mock_data_frame.assert_called_once_with(
        [
            {
                "repository": "Test1",
                "total_files": 10,
                "total_commits": 0,
                "commits": [],
                "languages": {
                    "count": catalogued_repository.language_count,
                    "sloc": catalogued_repository.language_sloc,
                },
            }
        ]
    )


@patch(f"{FILE_PATH}.get_commits")
@patch(f"{FILE_PATH}.git.Repo")
def test_create_repository_statistics(
    _mock_repo: MagicMock, mock_get_commits: MagicMock
) -> None:
    # Arrange
    repository_name = "Test1"
    path_to_repo = "TestPath"
    # Act
    catalogued_repository = create_repository_statistics(repository_name, path_to_repo)
    # Assert
    assert catalogued_repository.repository_name == repository_name
    assert catalogued_repository.total_files == 0
    assert catalogued_repository.total_commits == 1
    assert catalogued_repository.commits == mock_get_commits.return_value


@patch(f"{FILE_PATH}.dump")
@patch(f"{FILE_PATH}.Path")
def test_generate_output_file(mock_path: MagicMock, mock_dump: MagicMock) -> None:
    # Arrange
    configuration = MagicMock()
    data_frame = MagicMock()
    overall_statistics = MagicMock()
    # Act
    generate_output_file(configuration, data_frame, overall_statistics)
    # Assert
    mock_path.assert_called_once_with("statistics/repository_statistics.json")
    mock_path.return_value.open.assert_called_once_with("w")
    mock_dump.assert_called_once_with(
        {
            "repository_owner": configuration.repository_owner,
            "overall_statistics": overall_statistics,
            "repositories": data_frame.to_dict(orient="records"),
        },
        mock_path.return_value.open.return_value.__enter__.return_value,
    )
