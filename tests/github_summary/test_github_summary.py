from .utils import get_summary_markdown

owner = "JackPlowman"
repo = "github-stats-analyser"
run_id = 11996895865


def test_github_summary() -> None:
    # Act
    markdown = get_summary_markdown(owner, repo, run_id)
    # Assert
