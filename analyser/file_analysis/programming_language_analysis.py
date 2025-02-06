from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pygments import lexers
from pygments.util import ClassNotFound
from structlog import get_logger, stdlib

if TYPE_CHECKING:
    from .repository_languages import RepositoryLanguages
logger: stdlib.BoundLogger = get_logger()


def analyse_programming_languages(file_path: str, repository_languages: RepositoryLanguages) -> RepositoryLanguages:
    """Analyse the programming languages in a file.

    Args:
        file_path (str): The path to the file.
        repository_languages (RepositoryLanguages): The repository languages.

    Returns:
        RepositoryAnalysis: The repository analysis.
    """
    guess = guess_language_from_file(file_path)
    if guess:
        repository_languages.add_file(language_name=guess, file_path=file_path)
        sloc = count_sloc(file_path)
        repository_languages.add_sloc(language_name=guess, sloc=sloc)
        logger.debug("Added file to repository languages", file_path=file_path, language=guess, sloc=sloc)
    return repository_languages


def guess_language_from_file(file_path: str) -> str | None:
    """Guess the programming language from the file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str | None: The programming language, or None if no language is found.
    """
    try:
        with Path.open(file_path) as file:
            lexer = lexers.guess_lexer_for_filename(file_path, file.read())
            return lexer.name
    except (ClassNotFound, UnicodeDecodeError):
        logger.debug("Could not guess language from file", file_path=file_path)
        return None


def get_language_patterns(language: str | None) -> tuple[list[str], list[tuple[str, str]]]:
    """Get the comment patterns for a given language.

    Args:
        language (str | None): The programming language name

    Returns:
        tuple[list[str], list[tuple[str, str]]]: Single-line and multi-line comment patterns
    """
    # Default patterns (C-style)
    single_line = ["//", "#"]
    multi_line = [("/*", "*/"), ('"""', '"""'), ("'''", "'''")]

    patterns = {
        "Python": (["#"], [('"""', '"""'), ("'''", "'''")]),
        "JavaScript": (["//"], [("/*", "*/"), ("//", "\n")]),
        "HTML": ([], [("<!--", "-->")]),
        "CSS": ([], [("/*", "*/")]),
        "Ruby": (["#"], [("=begin", "=end")]),
        "PHP": (["//", "#"], [("/*", "*/")]),
        "Rust": (["//"], [("/*", "*/")]),
        "Go": (["//"], [("/*", "*/")]),
        "Swift": (["//"], [("/*", "*/")]),
    }

    return patterns.get(language, (single_line, multi_line))


def count_sloc(file_path: str) -> int:  # noqa: C901
    """Count source lines of code excluding comments and blank lines.

    Update to use Pygount when it supports Python 3.13.

    Args:
        file_path (str): Path to the source file

    Returns:
        int: Number of source lines of code
    """
    language = guess_language_from_file(file_path)
    single_line_patterns, multi_line_patterns = get_language_patterns(language)

    sloc = 0
    in_multiline_comment = False
    current_multi_pattern = None

    try:
        with Path(file_path).open() as file:
            content = file.readlines()
            i = 0
            while i < len(content):
                logger.warning("Reading line", line=content[i].strip())
                line = content[i].strip()

                # Skip empty lines
                if not line:
                    i += 1
                    continue

                # Handle multi-line comments
                if not in_multiline_comment:
                    for start, end in multi_line_patterns:
                        if line.startswith(start) or start in line:
                            in_multiline_comment = True
                            current_multi_pattern = end
                            break

                if in_multiline_comment:
                    if current_multi_pattern in line:
                        in_multiline_comment = False
                        current_multi_pattern = None
                    i += 1
                    continue

                # Handle single-line comments
                is_comment = False
                for pattern in single_line_patterns:
                    if line.lstrip().startswith(pattern):
                        is_comment = True
                        break

                if not is_comment:
                    sloc += 1

                i += 1

    except (OSError, UnicodeDecodeError):
        logger.exception("Error reading file", file_path=file_path)
        return 0

    return sloc
