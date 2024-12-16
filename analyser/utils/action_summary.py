from os import environ
from pathlib import Path

from pandas import DataFrame
from structlog import get_logger, stdlib
from .configuration import Configuration

logger: stdlib.BoundLogger = get_logger()


def generate_action_summary(configuration: Configuration, statistics_dataframe: DataFrame) -> None:
    """Generate the action summary.

    Args:
        configuration (Configuration): The configuration.
        statistics_dataframe (DataFrame): The statistics data frame.
    """
    with Path(environ["GITHUB_STEP_SUMMARY"]).open("w") as file:
        file_contents = f"""
        # GitHub Stats Analyser \n
        ## Action Configuration \n
        {configuration.generate_action_summary_table()}
        ## Statistics \n
        {statistics_dataframe.to_markdown()}
        """
        file.write(file_contents)
