from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class LanguageAnalysis(TypedDict):
    """The analysis of a programming language used in repository."""

    file_count: int
    file_paths: list[str]
    sloc: int = 0


@dataclass
class RepositoryLanguages:
    """The file language types generated from a repository."""

    languages: dict[str, LanguageAnalysis] = field(default_factory=dict)
    # example: {"Python": {"file_count": 1, "file_paths": ["file.py"], "sloc", 1}}

    def add_file(self, language_name: str, file_path: str) -> None:
        """Add a file to the repository languages.

        Args:
            language_name (str): The language name.
            file_path (str): The file path.
        """
        if language_name not in self.languages:
            self.languages[language_name] = {"file_count": 1, "file_paths": [file_path]}
            return
        language_file_count = self.languages[language_name]["file_count"]
        self.languages[language_name]["file_count"] = language_file_count + 1
        self.languages[language_name]["file_paths"].append(file_path)

    def add_sloc(self, language_name: str, sloc: int) -> None:
        """Add the source lines of code (SLOC) for a language.

        Args:
            language_name (str): The language name.
            sloc (int): The source lines of code.
        """
        if language_name in self.languages:
            if "sloc" in self.languages[language_name]:
                self.languages[language_name]["sloc"] += sloc
            else:
                self.languages[language_name]["sloc"] = sloc
        else:
            self.languages[language_name] = {"sloc": sloc}

    def __repr__(self) -> str:
        """Return a string representation of the repository languages."""
        languages_strings = [
            f"{language}: {self.languages[language]['file_count']}"
            for language in self.languages
        ]
        language_string = ", ".join(languages_strings)
        return f"RepositoryLanguages(languages={language_string})"

    def get_data(self) -> dict[str, int]:
        """Return the data for the repository languages."""
        return {
            language: self.languages[language]["file_count"]
            for language in self.languages
        }

    def get_sloc(self) -> dict[str, int]:
        """Return the SLOC for the repository languages."""
        return {
            language: self.languages[language]["sloc"] for language in self.languages
        }
