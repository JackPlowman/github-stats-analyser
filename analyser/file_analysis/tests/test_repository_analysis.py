from unittest.mock import MagicMock, patch

from analyser.file_analysis.repository_analysis import (
    RepositoryAnalysis,
    analyse_repository,
)

FILE_PATH = "analyser.file_analysis.repository_analysis"


def test_repository_analysis() -> None:
    # Arrange
    file_count = 10
    languages = MagicMock()
    # Act
    response = RepositoryAnalysis(file_count, languages)
    # Assert
    assert response.file_count == file_count
    assert response.languages == languages


@patch(f"{FILE_PATH}.RepositoryLanguages")
@patch(f"{FILE_PATH}.RepositoryAnalysis")
@patch(f"{FILE_PATH}.analyse_programming_languages")
def test_analyse_repository(
    mock_analyse_programming_languages: MagicMock,
    mock_repository_analysis: MagicMock,
    mock_repository_languages: MagicMock,
) -> None:
    # Arrange
    path_to_repo = "tester"
    # Act
    response = analyse_repository(path_to_repo)
    # Assert
    mock_repository_analysis.assert_called_once_with(
        0, mock_repository_languages.return_value
    )
    mock_analyse_programming_languages.assert_not_called()
    assert response == mock_repository_analysis.return_value
