from bs4 import BeautifulSoup
from requests import get

owner = "JackPlowman"
repo = "github-stats-analyser"
run_id = 11996895865


def test_github_summary() -> None:
    # Arrange

    response = get(f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/jobs", timeout=10)
    # assert response.status_code == 200
    # page = BeautifulSoup(response.text, "html.parser")
    # print(page)
    raise Exception("Test not implemented")
    # Act

    # Assert
