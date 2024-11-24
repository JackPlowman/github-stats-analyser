from os import environ

from pandas import DataFrame
from structlog import get_logger, stdlib

logger: stdlib.BoundLogger = get_logger()


def generate_action_summary(statistics_dataframe: DataFrame) -> None:
    """Generate the action summary.

    Args:
        statistics_dataframe (DataFrame): The statistics data frame.
    """
    environ["GITHUB_STEP_SUMMARY"] = statistics_dataframe.to_markdown()
    logger.warning(
        "Generated action summary",
        action_summary=environ["GITHUB_STEP_SUMMARY"],
        statistics=statistics_dataframe.to_markdown(),
    )
