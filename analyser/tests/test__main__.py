from os import environ
from unittest.mock import MagicMock, patch

import pytest

from analyser.__main__ import main

FILE_PATH = "analyser.__main__"


@patch(f"{FILE_PATH}.create_statistics")
def test_main(mock_create_statistics: MagicMock) -> None:
    # Arrange
    environ["INPUT_REPOSITORY_OWNER"] = "test2"
    # Act
    main()
    # Assert
    mock_create_statistics.assert_called_once()
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]


@patch(f"{FILE_PATH}.create_statistics")
def test_main__error(mock_create_statistics: MagicMock) -> None:
    # Arrange
    mock_create_statistics.side_effect = Exception("Test")
    environ["INPUT_REPOSITORY_OWNER"] = "test2"
    # Act
    with pytest.raises(Exception, match="Test"):
        main()
    # Assert
    mock_create_statistics.assert_called_once()
    # Clean Up
    del environ["INPUT_REPOSITORY_OWNER"]
