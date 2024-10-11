#!/bin/bash
set -e +x

# check file exists
test -f repository_statistics.json

# check file is not empty
test -s repository_statistics.json
