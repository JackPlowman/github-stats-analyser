from dataclasses import dataclass
from os import getenv
from typing import Self


@dataclass
class Configuration:
    """Configuration for the analyser."""

    repository_owner: str

    def __init__(self: Self) -> None:
        """Initialise the configuration."""
        self.repository_owner = self.get_and_check_for_value("INPUT_REPOSITORY_OWNER")

    def get_and_check_for_value(self: Self, key: str) -> str:
        """Get a value from the configuration and check it has been set.

        Args:
            key (str): The key to get the value for.

        Returns:
            str | None: The value for the key or None if it is not set.
        """
        value = getenv(key)
        if isinstance(value, str):
            return value
        updated_variable_key = key.removeprefix("INPUT_") if "INPUT_" in key else key
        msg = f"Configuration value for {updated_variable_key} is not set"
        raise ValueError(msg)
