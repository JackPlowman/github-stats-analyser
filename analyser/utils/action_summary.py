from os import environ

from pandas import DataFrame


def generate_action_summary(statistics_dataframe: DataFrame) -> None:
    """Generate the action summary.

    Args:
        statistics_dataframe (DataFrame): The statistics data frame.
    """
    environ["GITHUB_STEP_SUMMARY"] = statistics_dataframe.to_markdown()
