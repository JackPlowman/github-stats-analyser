#!/bin/sh
set -e +x

printenv

if [ "$CI" = "true" ]; then
  # if running in GitHub Actions, change to the root of the repository
  cd ..
  cd ..
fi

# Run the analyser
python -m analyser

# Check the output
ls -a

if [ "$CI" = "true" ]; then
  # if running in GitHub Actions, copy the output to the output directory
  cp statistics/repository_statistics.json github/workspace/repository_statistics.json
fi
