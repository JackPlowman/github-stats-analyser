# ------------------------------------------------------------------------------
# Common Commands
# ------------------------------------------------------------------------------

# Install python dependencies
install:
    poetry install

# Run the analyser
run:
    poetry run python -m analyser

# Run the analyser with default values
run-with-defaults:
    INPUT_DEBUG=true INPUT_REPOSITORY_OWNER=JackPlowman poetry run python -m analyser

# Run unit tests
unit-test:
    poetry run pytest analyser --cov=. --cov-report=xml

# Run unit tests with debug output
unit-test-debug:
    poetry run pytest analyser --cov=. --cov-report=xml -vvvv

# Validate the schema of the generated statistics file
validate-schema:
    poetry run check-jsonschema --schemafile test/schema_validation/repository_statistics_schema.json test/schema_validation/repository_statistics.json

# ------------------------------------------------------------------------------
# Cleaning Commands
# ------------------------------------------------------------------------------

# Remove all cloned repositories and generated files
clean:
    just clean-repos
    just clean-generated-files
    find . \( \
      -name '__pycache__' -o \
      -name '.coverage' -o \
      -name '.mypy_cache' -o \
      -name '.pytest_cache' -o \
      -name '.ruff_cache' -o \
      -name '*.pyc' -o \
      -name '*.pyd' -o \
      -name '*.pyo' -o \
      -name 'coverage.xml' -o \
      -name 'db.sqlite3' \
    \) -print | xargs rm -rfv

# Remove all cloned repositories
clean-repos:
    rm -rf cloned_repositories/** || true

# Remove all generated files from running analyser
clean-generated-files:
    rm statistics/*.csv || true

# ------------------------------------------------------------------------------
# Docker Commands
# ------------------------------------------------------------------------------

# Build the Docker image
docker-build:
    docker build -t jackplowman/github-stats-analyser:latest .

# Run the analyser in a Docker container, used for testing the github action docker image
docker-run:
    docker run \
      --env GITHUB_TOKEN=${GITHUB_TOKEN} \
      --env INPUT_REPOSITORY_OWNER=JackPlowman \
      --volume "$(pwd)/statistics:/statistics" \
      --volume "$(pwd)/cloned_repositories:/cloned_repositories" \
      --volume "$(pwd)/analyser:/analyser" \
      --rm jackplowman/github-stats-analyser:latest

# ------------------------------------------------------------------------------
# Ruff - Python Linting and Formating
# Set up ruff red-knot when it's ready
# ------------------------------------------------------------------------------

# Fix all Ruff issues
ruff-fix:
    just ruff-lint-fix
    just ruff-format-fix

# Check for Ruff issues
ruff-lint:
    poetry run ruff check analyser
    poetry run ruff check python_scripts

# Fix Ruff lint issues
ruff-lint-fix:
    poetry run ruff check analyser --fix
    poetry run ruff check python_scripts --fix

# Check for Ruff format issues
ruff-format:
    poetry run ruff format --check analyser
    poetry run ruff format --check python_scripts

# Fix Ruff format issues
ruff-format-fix:
    poetry run ruff format analyser
    poetry run ruff format python_scripts

# ------------------------------------------------------------------------------
# Other Python Tools
# ------------------------------------------------------------------------------

# Check for unused code
vulture:
    poetry run vulture analyser

# ------------------------------------------------------------------------------
# Prettier - File Formatting
# ------------------------------------------------------------------------------

# Check for prettier issues
prettier-check:
    prettier . --check

# Fix prettier issues
prettier-format:
    prettier . --check --write

# ------------------------------------------------------------------------------
# Justfile
# ------------------------------------------------------------------------------

# Format the Just code
format:
    just --fmt --unstable

# Check for Just format issues
format-check:
    just --fmt --check --unstable

# ------------------------------------------------------------------------------
# Git Hooks
# ------------------------------------------------------------------------------

# Install pre commit hook to run on all commits
install-git-hooks:
    cp -f githooks/pre-commit .git/hooks/pre-commit
    cp -f githooks/post-commit .git/hooks/post-commit
    chmod ug+x .git/hooks/*
