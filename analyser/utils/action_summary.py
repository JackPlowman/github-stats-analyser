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
    with Path(environ["GITHUB_STEP_SUMMARY"]).open("w") as file:
        file.write(statistics_dataframe.to_markdown())
