from os import environ
from pathlib import Path

from pandas import DataFrame
from structlog import get_logger, stdlib

logger: stdlib.BoundLogger = get_logger()


def generate_action_summary(statistics_dataframe: DataFrame) -> None:
    """Generate the action summary.

    Args:
        statistics_dataframe (DataFrame): The statistics data frame.
    """
    summary = statistics_dataframe.to_markdown()
    if "GITHUB_STEP_SUMMARY" in environ:
        logger.debug("Running in GitHub Actions, generating action summary")
        with Path(environ["GITHUB_STEP_SUMMARY"]).open("w") as file:
            file.write(summary)
    else:
        logger.debug(
            "Not running in GitHub Actions, skipping generating action summary"
        )
