#!/bin/sh

# Echo cwd
echo "Current working directory: $(pwd)"

# Show files
ls -la

# Run the analyser
poetry run python -m analyser