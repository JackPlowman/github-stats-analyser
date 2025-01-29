from unittest.mock import MagicMock, patch

from pygments.util import ClassNotFound

from analyser.file_analysis.programming_language_analysis import (
    analyse_programming_languages,
    count_sloc,
    get_language_patterns,
    guess_language_from_file,
)

FILE_PATH = "analyser.file_analysis.programming_language_analysis"


@patch(f"{FILE_PATH}.guess_language_from_file")
def test_analyse_programming_languages__no_guess(mock_guess_language_from_file: MagicMock) -> None:
    # Arrange
    mock_guess_language_from_file.return_value = None
    file_name = "test.py"
    repository_languages = MagicMock()
    # Act
    response = analyse_programming_languages(file_path=file_name, repository_languages=repository_languages)
    # Assert
    mock_guess_language_from_file.assert_called_once_with(file_name)
    assert response == repository_languages


@patch(f"{FILE_PATH}.count_sloc")
@patch(f"{FILE_PATH}.guess_language_from_file")
def test_analyse_programming_languages__with_guess(
    mock_guess_language_from_file: MagicMock, mock_count_sloc: MagicMock
) -> None:
    # Arrange
    mock_guess_language_from_file.return_value = language = "Python"
    file_name = "test.py"
    repository_languages = MagicMock()
    # Act
    response = analyse_programming_languages(file_path=file_name, repository_languages=repository_languages)
    # Assert
    mock_guess_language_from_file.assert_called_once_with(file_name)
    repository_languages.add_file.assert_called_once_with(language_name=language, file_path=file_name)
    repository_languages.add_sloc.assert_called_once_with(language_name=language, sloc=mock_count_sloc.return_value)
    assert response == repository_languages


@patch(f"{FILE_PATH}.Path")
@patch(f"{FILE_PATH}.lexers")
def test_guess_language_from_file(mock_lexers: MagicMock, mock_path: MagicMock) -> None:
    # Arrange
    mock_path.open.return_value = MagicMock()
    mock_lexers.guess_lexer_for_filename.return_value.name = python = "Python"
    file_name = "test.py"
    # Act
    response = guess_language_from_file(file_name)
    # Assert
    mock_lexers.guess_lexer_for_filename.assert_called_once_with(
        file_name, mock_path.open.return_value.__enter__.return_value.read.return_value
    )
    assert response == python


@patch(f"{FILE_PATH}.Path")
@patch(f"{FILE_PATH}.lexers")
def test_guess_language_from_file__no_language(mock_lexers: MagicMock, mock_path: MagicMock) -> None:
    # Arrange
    mock_path.open.return_value = MagicMock()
    mock_lexers.guess_lexer_for_filename.side_effect = ClassNotFound()
    file_name = "test.py"
    # Act
    response = guess_language_from_file(file_name)
    # Assert
    mock_lexers.guess_lexer_for_filename.assert_called_once_with(
        file_name, mock_path.open.return_value.__enter__.return_value.read.return_value
    )
    assert response is None


def test_get_language_patterns() -> None:
    # Arrange
    language = "Python"
    # Act
    single_line, multi_line = get_language_patterns(language)
    # Assert
    assert single_line == ["#"]
    assert multi_line == [('"""', '"""'), ("'''", "'''")]


@patch(f"{FILE_PATH}.Path")
def test_count_sloc(mock_path: MagicMock) -> None:
    # Arrange
    file_name = "test.py"
    # Act
    response = count_sloc(file_name)
    # Assert
    assert response == 0
    mock_path.open.assert_called_once_with(file_name)
