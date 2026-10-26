from unittest.mock import MagicMock, patch

from analyser.commits.commits import get_commits


@patch("analyser.commits.commits.Repo")
def test_get_commits_groups_authors_and_counts_missing_names(
    mock_repo: MagicMock,
) -> None:
    mock_repo.return_value.iter_commits.return_value = [
        MagicMock(author=MagicMock(name="unused")),
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]
    for commit, author_name in zip(
        mock_repo.return_value.iter_commits.return_value,
        ["Alice", "Bob", "Alice", None],
        strict=True,
    ):
        commit.author.name = author_name

    assert get_commits("example-repo") == {"Alice": 2, "Bob": 1, "Unknown": 1}
    mock_repo.assert_called_once_with("example-repo")
