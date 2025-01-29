from analyser.file_analysis.repository_languages import RepositoryLanguages
from analyser.utils.catalogued_repository import CataloguedRepository


def test_catalogued_repository() -> None:
    # Arrange
    repository_name = "Test1/Test2"
    total_files = 10
    total_commits = 100
    languages = RepositoryLanguages()
    languages.add_file(language_name="Python", file_path="file.py")
    languages.add_sloc(language_name="Python", sloc=100)
    commits = []
    # Act
    catalogued_repository = CataloguedRepository(repository_name, total_files, commits, total_commits, languages.get_data(),languages.get_sloc() )
    # Assert
    assert catalogued_repository.repository_name == repository_name
    assert catalogued_repository.total_files == total_files
    assert catalogued_repository.total_commits == total_commits
    assert catalogued_repository.language_count == {"Python": 1}
    assert catalogued_repository.language_sloc == {"Python": 100}
    assert catalogued_repository.commits == commits
