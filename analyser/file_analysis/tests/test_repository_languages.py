from analyser.file_analysis.repository_languages import RepositoryLanguages


def test_add_file_initializes_sloc() -> None:
    languages = RepositoryLanguages()
    languages.add_file("Python", "example.py")

    assert languages.get_data() == {"Python": 1}
    assert languages.get_sloc() == {"Python": 0}


def test_add_sloc_before_files() -> None:
    languages = RepositoryLanguages()
    languages.add_sloc("Python", 4)
    languages.add_file("Python", "example.py")
    languages.add_sloc("Python", 2)

    assert languages.get_data() == {"Python": 1}
    assert languages.get_sloc() == {"Python": 6}
    assert languages.languages["Python"]["file_paths"] == ["example.py"]
