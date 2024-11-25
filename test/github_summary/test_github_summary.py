from playwright.sync_api import Page


def test_github_summary(page: Page) -> None:
    # Open page
    page.goto("https://github.com/JackPlowman/github-stats-analyser/actions/runs/11996895865")
