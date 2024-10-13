from analyser.file_analysis.repository_languages import RepositoryLanguages
from analyser.utils.catalogued_repository import CataloguedRepository


def test_catalogued_repository() -> None:
    # Arrange
    repository_name = "Test1/Test2"
    total_files = 10
    total_commits = 100
    languages = RepositoryLanguages()
    languages.add_file(language_name="Python", file_path="file.py")
    commits = []
    # Act
    catalogued_repository = CataloguedRepository(repository_name, total_files, commits, total_commits, languages)
    # Assert
    assert catalogued_repository.repository_name == repository_name
    assert catalogued_repository.total_files == total_files
    assert catalogued_repository.total_commits == total_commits
    assert catalogued_repository.languages == languages
    assert catalogued_repository.commits == commits
