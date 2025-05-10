"""Repository actions."""

from __future__ import annotations

from pathlib import Path
from shutil import rmtree

from structlog import get_logger, stdlib

logger: stdlib.BoundLogger = get_logger()
DEFAULT_GLOBS_TO_EXCLUDE = [".git"]


def remove_excluded_files(
    path_to_repo: str, globs_to_exclude: list[str] = DEFAULT_GLOBS_TO_EXCLUDE
) -> None:
    """Remove excluded files from the repository.

    Args:
        path_to_repo (str): The path to the repository.
        globs_to_exclude (list[str]): The globs to exclude.
    """
    for glob_str in globs_to_exclude:
        for path in Path(path_to_repo).glob(glob_str):
            if path.is_file():
                path.unlink()
                logger.debug("Removing file", file_path=path)
            elif path.is_dir():
                rmtree(path)
                logger.debug("Removing directory", directory_path=path)
