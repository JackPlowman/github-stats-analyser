"""Application entry point."""

from pathlib import Path
from shutil import rmtree

from structlog import get_logger, stdlib

from .statistics import create_statistics
from .utils.action_summary import generate_action_summary
from .utils.configuration import Configuration
from .utils.custom_logging import set_up_custom_logging

logger: stdlib.BoundLogger = get_logger()


def main() -> None:
    """Entrypoint for Application."""
    try:
        set_up_custom_logging()
        configuration = Configuration()
        statistics = create_statistics(configuration)
        generate_action_summary(statistics)
    except Exception as error:
        logger.exception("An error occurred during the execution of the analyser.", error=error)
        raise
    finally:
        clean_up_cloned_repositories()


def clean_up_cloned_repositories() -> None:
    """Clean up."""
    objects = Path("cloned_repositories")
    to_delete = [obj for obj in objects.iterdir() if obj.is_dir()]
    for repository in to_delete:
        logger.debug("Removing directory", directory_path=repository)
        rmtree(repository)


if __name__ == "__main__":
    main()
