from requests import get


def get_summary_markdown(owner: str, repo: str, run_id: int) -> str:
    """Get the summary markdown from the GitHub Actions run.

    Args:
        owner (str): GitHub repository owner
        repo (str): GitHub repository name
        run_id (int): GitHub Actions run ID

    Returns:
        str: Summary markdown from the GitHub Actions run
    """
    github_summary_markdown_url = get_github_summary_markdown_url(owner, repo, run_id)
    github_summary_response = get(github_summary_markdown_url, timeout=10)
    github_summary_response.raise_for_status()
    return github_summary_response.text


def get_github_summary_markdown_url(owner: str, repo: str, run_id: int) -> str:
    """Get the URL of the GitHub summary markdown file.

    Args:
        owner (str): GitHub repository owner
        repo (str): GitHub repository name
        run_id (int): GitHub Actions run ID

    Returns:
        str: URL of the GitHub summary markdown file
    """
    workflow_response = get(f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/jobs", timeout=10)
    workflow_response.raise_for_status()
    jobs = workflow_response.json()["jobs"]
    jobs = [job for job in jobs if job["name"] == "Validate Schema"]
    if not jobs:
        msg = "No jobs found"
        raise ValueError(msg)
    if len(jobs) > 1:
        msg = "Multiple jobs found"
        raise ValueError(msg)
    job = jobs[0]
    step_id = job["html_url"].split("/")[-1]
    print(f"https://github.com/{owner}/{repo}/actions/runs/{run_id}/jobs/{step_id}/summary_raw")
    raise NotImplementedError("Function not implemented")

    # return job["html_url"]
    # print(f"{job["html_url"]}/summary_raw")
    # raise NotImplementedError("Function not implemented")
