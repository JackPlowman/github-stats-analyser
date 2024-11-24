from os import environ
from unittest.mock import MagicMock, patch

import pytest

from analyser.__main__ import main

FILE_PATH = "analyser.__main__"


@patch(f"{FILE_PATH}.generate_action_summary")
@patch(f"{FILE_PATH}.create_statistics")
@patch(f"{FILE_PATH}.Configuration")
def test_main(
    mock_configuration: MagicMock,
    mock_create_statistics: MagicMock,
    mock_generate_action_summary: MagicMock,
) -> None:
    # Arrange
    environ["INPUT_REPOSITORY_OWNER"] = "test2"
    # Act
    main()
    # Assert
    mock_configuration.assert_called_once_with()
    mock_create_statistics.assert_called_once_with(mock_configuration.return_value)
    mock_generate_action_summary.assert_called_once_with(mock_create_statistics.return_value)
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]


@patch(f"{FILE_PATH}.generate_action_summary")
@patch(f"{FILE_PATH}.create_statistics")
@patch(f"{FILE_PATH}.Configuration")
def test_main__error(
    mock_configuration: MagicMock,
    mock_create_statistics: MagicMock,
    mock_generate_action_summary: MagicMock,
) -> None:
    # Arrange
    mock_create_statistics.side_effect = Exception("Test")
    environ["INPUT_REPOSITORY_OWNER"] = "test2"
    # Act
    with pytest.raises(Exception, match="Test"):
        main()
    # Assert
    mock_configuration.assert_called_once_with()
    mock_create_statistics.assert_called_once_with(mock_configuration.return_value)
    mock_generate_action_summary.assert_not_called()
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]
