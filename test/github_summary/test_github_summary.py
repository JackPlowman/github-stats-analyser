from requests import get


def test_github_summary() -> None:
    # Arrange
    response = get("https://github.com/JackPlowman/github-stats-analyser/actions/runs/11996895865", timeout=10)
    assert response.status_code == 200
    # Act
    # Assert
