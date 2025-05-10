from os import environ
from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd

from analyser.utils.action_summary import generate_action_summary

FILE_PATH = "analyser.utils.action_summary"


@patch(f"{FILE_PATH}.Path")
def test_generate_action_summary_github_actions(mock_path: MagicMock) -> None:
    # Arrange
    environ["GITHUB_STEP_SUMMARY"] = summary_file = "summary.md"
    dataframe = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    expected_summary = dataframe.to_markdown()
    # Act
    generate_action_summary(dataframe)
    # Assert
    mock_path.assert_called_once_with(summary_file)
    mock_path.return_value.open.assert_called_once_with("w")
    mock_path.return_value.open.return_value.__enter__.return_value.write.assert_called_once_with(
        expected_summary
    )
    # Cleanup
    if Path(summary_file).exists():
        Path(summary_file).unlink()
    environ.pop("GITHUB_STEP_SUMMARY")


@patch(f"{FILE_PATH}.Path")
def test_generate_action_summary_not_github_actions(mock_path: MagicMock) -> None:
    # Arrange
    environ.pop("GITHUB_STEP_SUMMARY", None)
    # Act
    generate_action_summary(pd.DataFrame())
    # Assert
    mock_path.assert_not_called()
