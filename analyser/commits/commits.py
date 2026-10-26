from __future__ import annotations

from git import Repo


def get_commits(path_to_repo: str) -> dict[str, int]:
    """Get the number of commits in a repository.

    Args:
        path_to_repo (str): The path to the repository.

    Returns:
        list[UserCommits]: The list of user commits.
    """
    repo = Repo(path_to_repo)
    commits = repo.iter_commits()

    user_commits = {}
    for commit in commits:
        author_name = commit.author.name or "Unknown"
        if author_name not in user_commits:
            user_commits[author_name] = 1
        else:
            user_commits[author_name] += 1

    return user_commits
