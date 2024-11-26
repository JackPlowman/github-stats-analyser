from markdown import markdown

from .utils import get_summary_markdown

owner = "JackPlowman"
repo = "github-stats-analyser"
run_id = 11996895865


def test_github_summary() -> None:
    # Act
    summary_markdown = get_summary_markdown(owner, repo, run_id)
    # Assert
    # table_html = markdown(summary_markdown, extensions=["markdown.extensions.tables"])
    # print(table_html)
    # raise NotImplementedError("Test not implemented")
