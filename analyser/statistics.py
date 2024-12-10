from json import dump
from pathlib import Path

import git
from pandas import DataFrame
from structlog import get_logger, stdlib

from analyser.commits.commits import get_commits
from analyser.file_analysis.repository_analysis import analyse_repository
from analyser.utils.catalogued_repository import CataloguedRepository
from analyser.utils.configuration import Configuration
from analyser.utils.github_interactions import clone_repo, retrieve_repositories
from analyser.utils.repository_actions import remove_excluded_files

logger: stdlib.BoundLogger = get_logger()
DEFAULT_FILE_LOCATION = "statistics/repository_statistics.json"


def create_statistics(configuration: Configuration) -> DataFrame:
    """Create statistics."""
    # Retrieve the list of repositories to analyse
    repositories = retrieve_repositories(configuration)
    # Set up data frame
    list_of_repositories = []
    # Create statistics for each repository
    for repository in repositories:
        owner_name, repository_name = repository.owner.login, repository.name
        # Clone the repository to cloned_repositories
        path = clone_repo(owner_name, repository_name)
        # Create statistics for the repository
        catalogued_repository = create_repository_statistics(repository_name, path)
        list_of_repositories.append(catalogued_repository)

    logger.debug("List of repositories", list_of_repositories=list_of_repositories)

    dataframe = DataFrame(
        [
            {
                "repository": repository.repository_name,
                "total_files": repository.total_files,
                "total_commits": repository.total_commits,
                "commits": repository.commits,
                "languages": repository.languages,
            }
            for repository in list_of_repositories
        ]
    )
    generate_output_file(configuration, dataframe)
    logger.debug("Saved statistics to file", file_location=DEFAULT_FILE_LOCATION)
    return dataframe


def create_repository_statistics(repository_name: str, path_to_repo: str) -> CataloguedRepository:
    """Create statistics for a repository.

    Args:
        repository_name (str): The name of the repository.
        path_to_repo (str): The path to the repository.

    Returns:
        CataloguedRepository: The catalogued repository.
    """
    logger.info("Analysing repository", repository_name=repository_name)
    # Retrieve the total number of commits
    repo = git.Repo(path_to_repo)
    total_commits = int(repo.git.rev_list("--count", "HEAD"))
    # Get commits for the repository
    commits = get_commits(path_to_repo)
    # Remove excluded files
    remove_excluded_files(path_to_repo)
    # Analyse the repository files
    analysed_repository = analyse_repository(path_to_repo)
    # Return the catalogued repository
    return CataloguedRepository(
        repository_name=repository_name,
        total_files=analysed_repository.file_count,
        total_commits=total_commits,
        commits=commits,
        languages=analysed_repository.languages.get_data(),
    )


def generate_output_file(configuration: Configuration, dataframe: DataFrame) -> None:
    """Generate an output file.

    Args:
        configuration (Configuration): The configuration.
        dataframe (DataFrame): The data frame.
    """
    with Path(DEFAULT_FILE_LOCATION).open("w") as file:
        dump(
            {
                "repository_owner": configuration.repository_owner,
                "repositories": dataframe.to_dict(orient="records"),
            },
            file,
        )
