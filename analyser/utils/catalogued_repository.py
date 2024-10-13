from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from analyser.file_analysis.repository_languages import RepositoryLanguages


@dataclass
class CataloguedRepository:
    """A catalogued repository."""

    repository_name: str
    total_files: int
    commits: dict[str, int]
    total_commits: int
    languages: RepositoryLanguages
