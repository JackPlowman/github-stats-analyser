#!/bin/sh
set -e +x

if [ "$CI" = "true" ]; then
  # if running in GitHub Actions, change to the root of the repository
  cd ..
  cd ..
fi

# Check that the required environment variables are set
python check_environment_variables.py

# Run the analyser
python -m analyser

if [ "$CI" = "true" ]; then
  # if running in GitHub Actions, copy the output to the output directory
  cp statistics/repository_statistics.json github/workspace/repository_statistics.json
  echo "Copied statistics to github/workspace"
fi
