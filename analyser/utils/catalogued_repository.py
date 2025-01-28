from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CataloguedRepository:
    """A catalogued repository."""

    repository_name: str
    total_files: int
    commits: dict[str, int]
    total_commits: int
    language_count: dict[str, int]
    language_sloc: dict[str, int]
